"""Evolution engine: one seed = three populations evolving in lockstep."""
from __future__ import annotations

import asyncio
import gzip
import json
import time
from dataclasses import dataclass, field
from pathlib import Path

from . import game
from .genome import EditError, Genome, IdFactory, apply_edit, clone_genome, root_genome
from .llm import Gateway

SURVIVE = "Survive."


class InvalidRateStop(RuntimeError):
    pass


@dataclass
class Agent:
    id: str
    slot: int
    genome: Genome
    born_gen: int
    parent_agent: str | None
    record: list = field(default_factory=list)  # exposed TAKE events
    stock: dict = field(default_factory=dict)
    # per-generation scratch
    payoffs: list = field(default_factory=list)
    history: list = field(default_factory=list)

    def to_dict(self):
        return {"id": self.id, "slot": self.slot, "genome": self.genome.to_dict(), "born_gen": self.born_gen,
                "parent_agent": self.parent_agent, "record": self.record, "stock": self.stock}

    @staticmethod
    def from_dict(d):
        return Agent(id=d["id"], slot=d["slot"], genome=Genome.from_dict(d["genome"]), born_gen=d["born_gen"],
                     parent_agent=d["parent_agent"], record=d["record"], stock=d["stock"])


def _write_jsonl_gz(path: Path, records: list[dict], mode="at"):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, mode, encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


class SeedRun:
    def __init__(self, *, seed: int, cfg: dict, n_gens: int, player_model: str, gateway: Gateway,
                 out_dir: Path, log_path: Path, populations: list[str] | None = None, tag: str = "main"):
        self.seed = seed
        self.cfg = cfg
        self.n_gens = n_gens
        self.player_model = player_model
        self.gw = gateway
        self.out = out_dir
        self.log_path = log_path
        self.pops = populations or list(cfg["populations"])
        self.tag = tag
        self.sched = game.Schedule(seed, cfg)
        self.ckpt_path = self.out / "checkpoint.json"
        self.state: dict[str, list[Agent]] = {}
        self.ids: dict[str, IdFactory] = {}
        self.next_gen = 0

    # ------------------------------------------------------------ state
    def init_state(self):
        g0 = self.cfg["initial_genome"]
        for p in self.pops:
            ids = IdFactory(f"s{self.seed}{p[0]}")
            self.ids[p] = ids
            agents = []
            for slot in range(self.cfg["pop_size"]):
                gnm = root_genome(g0, p, ids) if slot == 0 else clone_genome(agents[0].genome, 0, ids)
                if slot > 0:
                    # all initial agents share the root sentence ID; genome objects are distinct
                    gnm.parent_id = None
                    gnm.edit = {"op": "root"}
                agents.append(Agent(id=ids.agent(), slot=slot, genome=gnm, born_gen=0, parent_agent=None,
                                    stock=dict(self.cfg["game"]["initial_stock"])))
            self.state[p] = agents
        self.next_gen = 0

    def save_checkpoint(self):
        d = {"seed": self.seed, "n_gens": self.n_gens, "player_model": self.player_model, "next_gen": self.next_gen,
             "pops": {p: [a.to_dict() for a in ags] for p, ags in self.state.items()},
             "ids": {p: f.counters for p, f in self.ids.items()}}
        tmp = self.ckpt_path.with_suffix(".tmp")
        self.out.mkdir(parents=True, exist_ok=True)
        tmp.write_text(json.dumps(d))
        tmp.replace(self.ckpt_path)

    def load_checkpoint(self) -> bool:
        if not self.ckpt_path.exists():
            return False
        d = json.loads(self.ckpt_path.read_text())
        assert d["seed"] == self.seed and d["n_gens"] == self.n_gens and d["player_model"] == self.player_model
        self.state = {p: [Agent.from_dict(a) for a in ags] for p, ags in d["pops"].items()}
        self.ids = {p: IdFactory(f"s{self.seed}{p[0]}", c) for p, c in d["ids"].items()}
        self.next_gen = d["next_gen"]
        return True

    # ------------------------------------------------------------ player calls
    async def _player(self, kind, system, user, schema, max_tokens, meta):
        return await self.gw.call(model=self.player_model, system=system, user=user, schema=schema,
                                  max_tokens=max_tokens, meta={"kind": kind, **meta})

    async def _declare(self, system, rules, ctx, meta):
        r = await self._player("declare", system, game.declare_prompt(rules, ctx), game.DECLARE_SCHEMA,
                               self.cfg["player"]["max_tokens_declare"], meta)
        p = game.parse_declare(r.text, r.stop_reason, self.cfg["game"]["declare_max_words"])
        if r.error:
            p.update(valid=False, reason="api_error:" + r.error, value="ASK", message="")
        p["raw"] = r.text
        p["cost"] = r.cost
        return p

    async def _act(self, system, rules, ctx, meta):
        r = await self._player("action", system, game.action_prompt(rules, ctx), game.ACTION_SCHEMA,
                               self.cfg["player"]["max_tokens_action"], meta)
        p = game.parse_action(r.text, r.stop_reason)
        if r.error:
            p.update(valid=False, reason="api_error:" + r.error, value="ASK")
        p["raw"] = r.text
        p["cost"] = r.cost
        return p

    # ------------------------------------------------------------ main game
    async def _encounter(self, pop, gen, rd, pair_idx, a: Agent, b: Agent, rules, table):
        cur = self.sched.currency(gen, rd, pair_idx)
        win = self.cfg["game"]["reputation_window"]
        n = self.cfg["game"]["encounters_per_agent"]
        base = {"seed": self.seed, "pop": pop, "gen": gen, "round": rd, "phase": self.tag}

        def ctx(me: Agent, other: Agent):
            return {"k": rd + 1, "n": n, "stock": me.stock, "currency": cur,
                    "own_record": game.format_record(me.record, win),
                    "partner_record": game.format_record(other.record, win)}

        ca, cb = ctx(a, b), ctx(b, a)
        da, db = await asyncio.gather(
            self._declare(a.genome.text, rules, ca, {**base, "agent": a.id, "partner": b.id}),
            self._declare(b.genome.text, rules, cb, {**base, "agent": b.id, "partner": a.id}))
        ca.update(own_decl=da["value"], own_msg=da["message"], partner_decl=db["value"], partner_msg=db["message"])
        cb.update(own_decl=db["value"], own_msg=db["message"], partner_decl=da["value"], partner_msg=da["message"])
        xa, xb = await asyncio.gather(
            self._act(a.genome.text, rules, ca, {**base, "agent": a.id, "partner": b.id}),
            self._act(b.genome.text, rules, cb, {**base, "agent": b.id, "partner": a.id}))
        pa, pb = game.payoff(xa["value"], xb["value"], table)
        ua, ub = self.sched.exposure_draw(gen, rd, a.slot), self.sched.exposure_draw(gen, rd, b.slot)
        p_exp = self.cfg["game"]["expose_prob"]
        ea = xa["value"] == "TAKE" and ua < p_exp
        eb = xb["value"] == "TAKE" and ub < p_exp
        rec = {
            **base, "pair": pair_idx, "currency": cur,
            "a": {"agent": a.id, "slot": a.slot, "genome": a.genome.id, "declare": da["value"], "message": da["message"],
                  "action": xa["value"], "payoff": pa, "exposed": ea,
                  "valid_declare": da["valid"], "valid_action": xa["valid"],
                  "invalid_reasons": [r for r in (da["reason"], xa["reason"]) if r],
                  "flags": sorted(set(da["flags"] + xa["flags"]))},
            "b": {"agent": b.id, "slot": b.slot, "genome": b.genome.id, "declare": db["value"], "message": db["message"],
                  "action": xb["value"], "payoff": pb, "exposed": eb,
                  "valid_declare": db["valid"], "valid_action": xb["valid"],
                  "invalid_reasons": [r for r in (db["reason"], xb["reason"]) if r],
                  "flags": sorted(set(db["flags"] + xb["flags"]))},
        }
        return rec, (a, da, xa, pa, ea, b), (b, db, xb, pb, eb, a)

    def _book(self, me: Agent, d, x, pay, exposed, other: Agent, od, ox, opay, cur, gen):
        me.payoffs.append(pay)
        me.stock[cur] = me.stock.get(cur, 0) + pay
        me.history.append({"partner_decl": od["value"], "partner_msg": od["message"], "own_decl": d["value"],
                           "own_msg": d["message"], "partner_action": ox["value"], "own_action": x["value"],
                           "own_payoff": pay})
        if exposed:
            me.record.append({"gen": gen, "declared": d["value"]})

    async def play_generation(self, gen: int, table: dict, rules: str) -> list[dict]:
        for p in self.pops:
            for a in self.state[p]:
                a.payoffs, a.history = [], []
        encounters = []
        for rd, pairs in enumerate(self.sched.pairings(gen)):
            tasks = []
            for p in self.pops:
                by_slot = {a.slot: a for a in self.state[p]}
                for i, (s1, s2) in enumerate(pairs):
                    tasks.append(self._encounter(p, gen, rd, i, by_slot[s1], by_slot[s2], rules, table))
            results = await asyncio.gather(*tasks)
            # book after the whole round: exposures become visible from the next round on
            for rec, A, B in results:
                cur = rec["currency"]
                a, da, xa, pa, ea, _ = A
                b, db, xb, pb, eb, _ = B
                self._book(a, da, xa, pa, ea, b, db, xb, pb, cur, gen)
                self._book(b, db, xb, pb, eb, a, da, xa, pa, cur, gen)
                encounters.append(rec)
        return encounters

    # ------------------------------------------------------------ benchmark
    async def benchmark_genome_parallel(self, pop, gen, agent: Agent, table, rules) -> dict:
        """Deviation used only by the subagent mini-run: all benchmark encounters of a genome are played
        at once (2 batched steps instead of 2 x 6 sequential ones). The genome keeps a fresh, empty
        record; TIT_FOR_TAT declares GIVE and then plays the genome's declaration of that encounter."""
        win = self.cfg["game"]["reputation_window"]
        base = {"seed": self.seed, "pop": pop, "gen": gen, "phase": "benchmark", "agent": agent.id}
        order = self.sched.bench_order
        stock = dict(self.cfg["game"]["initial_stock"])
        ctxs, sctx, metas, opp = [], {}, [], {}
        for k, o in enumerate(order):
            cur = self.sched.bench_currency(gen, agent.slot, k)
            opp_record = game.format_record([{"gen": -1, "declared": "TAKE"}] * 3, win) if o == "ALWAYS_TAKE" \
                else game.format_record([], win)
            ctxs.append({"k": k + 1, "n": len(order), "stock": stock, "currency": cur,
                         "own_record": game.format_record([], win), "partner_record": opp_record})
            metas.append({**base, "bench_k": k, "opponent": o})
            if o == "SURVIVE_AGENT":
                sctx[k] = {"k": k + 1, "n": len(order), "stock": stock, "currency": cur,
                           "own_record": game.format_record([], win), "partner_record": game.format_record([], win)}
        jobs = [self._declare(agent.genome.text, rules, ctxs[k], metas[k]) for k in range(len(order))]
        skeys = sorted(sctx)
        jobs += [self._declare(SURVIVE, rules, sctx[k], {**metas[k], "agent": "BENCH_SURVIVE", "vs_agent": agent.id}) for k in skeys]
        res = await asyncio.gather(*jobs)
        dg = res[: len(order)]
        ds = dict(zip(skeys, res[len(order):]))
        for k, o in enumerate(order):
            if o == "ALWAYS_GIVE":
                opp[k] = ("GIVE", "I always give.", "GIVE")
            elif o == "ALWAYS_TAKE":
                opp[k] = ("TAKE", "I always take.", "TAKE")
            elif o == "TIT_FOR_TAT":
                opp[k] = ("GIVE", "I mirror what you declare.", dg[k]["value"])
            elif o == "RANDOM":
                d, x = self.sched.bench_random(gen, agent.slot, k)
                opp[k] = (d, "", x)
            elif o == "SURVIVE_AGENT":
                opp[k] = (ds[k]["value"], ds[k]["message"], None)
            ctxs[k].update(own_decl=dg[k]["value"], own_msg=dg[k]["message"], partner_decl=opp[k][0],
                           partner_msg=opp[k][1])
            if k in sctx:
                sctx[k].update(own_decl=ds[k]["value"], own_msg=ds[k]["message"], partner_decl=dg[k]["value"],
                               partner_msg=dg[k]["message"])
        jobs = [self._act(agent.genome.text, rules, ctxs[k], metas[k]) for k in range(len(order))]
        jobs += [self._act(SURVIVE, rules, sctx[k], {**metas[k], "agent": "BENCH_SURVIVE", "vs_agent": agent.id}) for k in skeys]
        res = await asyncio.gather(*jobs)
        xg = res[: len(order)]
        xs = dict(zip(skeys, res[len(order):]))
        rows = []
        for k, o in enumerate(order):
            o_decl, o_msg, o_act = opp[k]
            o_valid = True
            if k in xs:
                o_act = xs[k]["value"]
                o_valid = ds[k]["valid"] and xs[k]["valid"]
            pg, po = game.payoff(xg[k]["value"], o_act, table)
            exposed = xg[k]["value"] == "TAKE" and self.sched.bench_exposure(gen, agent.slot, k) < self.cfg["game"]["expose_prob"]
            rows.append({"k": k, "opponent": o, "currency": ctxs[k]["currency"], "declare": dg[k]["value"],
                         "message": dg[k]["message"], "action": xg[k]["value"], "opp_declare": o_decl,
                         "opp_message": o_msg, "opp_action": o_act, "payoff": pg, "opp_payoff": po,
                         "exposed": exposed, "valid_declare": dg[k]["valid"], "valid_action": xg[k]["valid"],
                         "opp_valid": o_valid,
                         "invalid_reasons": [r for r in (dg[k]["reason"], xg[k]["reason"]) if r],
                         "flags": sorted(set(dg[k]["flags"] + xg[k]["flags"]))})
        score = sum(r["payoff"] for r in rows) / len(rows)
        return {"seed": self.seed, "pop": pop, "gen": gen, "agent": agent.id, "genome": agent.genome.id,
                "slot": agent.slot, "score": score, "encounters": rows}

    async def benchmark_genome(self, pop, gen, agent: Agent, table, rules) -> dict:
        if self.cfg["benchmark"].get("mode") == "parallel":
            return await self.benchmark_genome_parallel(pop, gen, agent, table, rules)
        win = self.cfg["game"]["reputation_window"]
        rec_events: list = []
        prev_action = None
        rows = []
        base = {"seed": self.seed, "pop": pop, "gen": gen, "phase": "benchmark", "agent": agent.id}
        for k, opp in enumerate(self.sched.bench_order):
            cur = self.sched.bench_currency(gen, agent.slot, k)
            opp_record = game.format_record([{"gen": -1, "declared": "TAKE"}] * 3, win) if opp == "ALWAYS_TAKE" \
                else game.format_record([], win)
            stock = dict(self.cfg["game"]["initial_stock"])
            ctx = {"k": k + 1, "n": len(self.sched.bench_order), "stock": stock, "currency": cur,
                   "own_record": game.format_record(rec_events, win), "partner_record": opp_record}
            survive_ctx = None
            meta = {**base, "bench_k": k, "opponent": opp}
            if opp == "SURVIVE_AGENT":
                survive_ctx = {"k": k + 1, "n": len(self.sched.bench_order), "stock": stock, "currency": cur,
                               "own_record": game.format_record([], win),
                               "partner_record": game.format_record(rec_events, win)}
                dg, do = await asyncio.gather(
                    self._declare(agent.genome.text, rules, ctx, meta),
                    self._declare(SURVIVE, rules, survive_ctx, {**meta, "agent": "BENCH_SURVIVE"}))
                o_decl, o_msg = do["value"], do["message"]
            else:
                dg = await self._declare(agent.genome.text, rules, ctx, meta)
                if opp == "ALWAYS_GIVE":
                    o_decl, o_msg, o_act = "GIVE", "I always give.", "GIVE"
                elif opp == "ALWAYS_TAKE":
                    o_decl, o_msg, o_act = "TAKE", "I always take.", "TAKE"
                elif opp == "TIT_FOR_TAT":
                    o_act = prev_action or "GIVE"
                    o_decl, o_msg = o_act, "I mirror your last move."
                elif opp == "RANDOM":
                    o_decl, o_act = self.sched.bench_random(gen, agent.slot, k)
                    o_msg = ""
                else:
                    raise ValueError(opp)
            ctx.update(own_decl=dg["value"], own_msg=dg["message"], partner_decl=o_decl, partner_msg=o_msg)
            if opp == "SURVIVE_AGENT":
                survive_ctx.update(own_decl=o_decl, own_msg=o_msg, partner_decl=dg["value"], partner_msg=dg["message"])
                xg, xo = await asyncio.gather(
                    self._act(agent.genome.text, rules, ctx, meta),
                    self._act(SURVIVE, rules, survive_ctx, {**meta, "agent": "BENCH_SURVIVE"}))
                o_act = xo["value"]
                o_valid = do["valid"] and xo["valid"]
            else:
                xg = await self._act(agent.genome.text, rules, ctx, meta)
                o_valid = True
            pg, po = game.payoff(xg["value"], o_act, table)
            exposed = xg["value"] == "TAKE" and self.sched.bench_exposure(gen, agent.slot, k) < self.cfg["game"]["expose_prob"]
            if exposed:
                rec_events.append({"gen": gen, "declared": dg["value"]})
            prev_action = xg["value"]
            rows.append({"k": k, "opponent": opp, "currency": cur, "declare": dg["value"], "message": dg["message"],
                         "action": xg["value"], "opp_declare": o_decl, "opp_message": o_msg, "opp_action": o_act,
                         "payoff": pg, "opp_payoff": po, "exposed": exposed,
                         "valid_declare": dg["valid"], "valid_action": xg["valid"], "opp_valid": o_valid,
                         "invalid_reasons": [r for r in (dg["reason"], xg["reason"]) if r],
                         "flags": sorted(set(dg["flags"] + xg["flags"]))})
        score = sum(r["payoff"] for r in rows) / len(rows)
        return {"seed": self.seed, "pop": pop, "gen": gen, "agent": agent.id, "genome": agent.genome.id,
                "slot": agent.slot, "score": score, "encounters": rows}

    # ------------------------------------------------------------ selection & mutation
    def rank(self, pop: str, gen: int) -> list[tuple[Agent, float]]:
        ags = self.state[pop]
        fit = [(a, sum(a.payoffs) / max(1, len(a.payoffs))) for a in ags]
        fit.sort(key=lambda t: (-t[1], self.sched.tiebreak(gen, t[0].slot)))
        return fit

    async def mutate(self, pop, gen, parent: Agent, notes: str, rules: str) -> Genome:
        ids = self.ids[pop]
        mcfg = self.cfg["mutator"]
        user = game.mutator_prompt(parent.genome.numbered(), notes, rules, self.cfg)
        tries = 0
        last_err = None
        while tries <= mcfg["structural_retries"]:
            tries += 1
            r = await self.gw.call(model=mcfg["model"], system=game.MUTATOR_SYSTEM, user=user,
                                   schema=game.MUTATION_SCHEMA, max_tokens=mcfg["max_tokens"],
                                   meta={"kind": "mutate", "seed": self.seed, "pop": pop, "gen": gen,
                                         "parent_agent": parent.id, "parent_genome": parent.genome.id,
                                         "try": tries, "phase": self.tag})
            if r.stop_reason == "refusal":
                g = clone_genome(parent.genome, gen + 1, ids)
                g.flags += ["mutation_refused"] + game.text_flags(r.text)
                g.edit = {"op": "clone", "reason": "refusal"}
                return g
            obj = game._load_json(r.text) if not r.error else None
            if not isinstance(obj, dict):
                last_err = r.error or "unparsable"
                continue
            try:
                return apply_edit(parent.genome, obj.get("op"), obj.get("target_id"), obj.get("new_sentence", ""),
                                  gen + 1, ids, self.cfg["genome_word_cap"], self.cfg["new_sentence_word_cap"])
            except EditError as e:
                last_err = str(e)
        g = clone_genome(parent.genome, gen + 1, ids)
        g.flags.append("mutation_failed")
        g.edit = {"op": "clone", "reason": f"mutation_failed: {last_err}"}
        return g

    # ------------------------------------------------------------ one generation
    async def run_generation(self, gen: int) -> dict:
        table, shocked = game.payoff_table(self.cfg, gen, self.n_gens)
        rules = game.rules_text(table, self.cfg)
        t0 = time.time()
        encounters = await self.play_generation(gen, table, rules)

        ranked = {p: self.rank(p, gen) for p in self.pops}
        n_rep, n_die = self.cfg["n_reproduce"], self.cfg["n_die"]
        survivors = {p: [a for a, _ in ranked[p][: len(ranked[p]) - n_die]] for p in self.pops}

        bench_tasks = [self.benchmark_genome(p, gen, a, table, rules) for p in self.pops for a in survivors[p]]
        bench = await asyncio.gather(*bench_tasks)

        # invalid-rate check per population (game + benchmark player calls of this generation)
        inv = self.invalid_rates(encounters, bench)
        bad = {p: v for p, v in inv.items() if v["rate"] > self.cfg["game"]["invalid_rate_stop"]}

        # genomes of this generation (the 24 that played), with fate
        gen_genomes = {}
        bench_by_agent = {b["agent"]: b["score"] for b in bench}
        for p in self.pops:
            rows = []
            for rank, (a, f) in enumerate(ranked[p], 1):
                fate = "parent" if rank <= n_rep else ("dies" if rank > len(ranked[p]) - n_die else "survives")
                rows.append({"agent": a.id, "slot": a.slot, "rank": rank, "fitness": f, "fate": fate,
                             "born_gen": a.born_gen, "parent_agent": a.parent_agent,
                             "bench_score": bench_by_agent.get(a.id), "genome": a.genome.to_dict()})
            gen_genomes[p] = rows

        mutations = []
        if not bad:
            # LAMARCK notes first (DARWIN filler lengths are matched to them by rank)
            notes_len_by_rank = {}
            if "LAMARCK" in self.pops:
                for rank, (a, f) in enumerate(ranked["LAMARCK"][:n_rep], 1):
                    notes_len_by_rank[rank] = len(game.lamarck_notes(f, rank, len(ranked["LAMARCK"]), a.history[-3:]))
            jobs = []
            for p in self.pops:
                for rank, (a, f) in enumerate(ranked[p][:n_rep], 1):
                    if p == "CONTROL":
                        continue
                    if p == "LAMARCK":
                        notes = game.lamarck_notes(f, rank, len(ranked[p]), a.history[-3:])
                    else:
                        L = notes_len_by_rank.get(rank) or len(game.lamarck_notes(f, rank, len(ranked[p]), a.history[-3:]))
                        notes = game.neutral_filler(L, self.sched.filler_offset(gen, rank))
                    jobs.append((p, rank, a, notes))
            results = await asyncio.gather(*[self.mutate(p, gen, a, notes, rules) for p, _, a, notes in jobs])
            child_genome = {(p, rank): g for (p, rank, _, _), g in zip(jobs, results)}
            for (p, rank, a, notes), g in zip(jobs, results):
                mutations.append({"seed": self.seed, "pop": p, "gen": gen, "parent_rank": rank, "parent_agent": a.id,
                                  "parent_genome": a.genome.id, "child_genome": g.id, "edit": g.edit, "flags": g.flags,
                                  "notes_len": len(notes)})
            # next generation
            for p in self.pops:
                dead = [a for a, _ in ranked[p][len(ranked[p]) - n_die:]]
                parents = [a for a, _ in ranked[p][:n_rep]]
                new_agents = list(survivors[p])
                for rank, (parent, slot_owner) in enumerate(zip(parents, sorted(dead, key=lambda x: x.slot)), 1):
                    if p == "CONTROL":
                        g = clone_genome(parent.genome, gen + 1, self.ids[p])
                    else:
                        g = child_genome[(p, rank)]
                    new_agents.append(Agent(id=self.ids[p].agent(), slot=slot_owner.slot, genome=g, born_gen=gen + 1,
                                            parent_agent=parent.id, stock=dict(self.cfg["game"]["initial_stock"])))
                new_agents.sort(key=lambda x: x.slot)
                self.state[p] = new_agents

        summary = {"seed": self.seed, "gen": gen, "shocked": shocked, "elapsed_s": round(time.time() - t0, 1),
                   "invalid": inv, "spent_usd": round(self.gw.budget.spent, 4)}
        self.persist_generation(gen, encounters, bench, gen_genomes, mutations, summary)
        if bad:
            self.write_diagnosis(gen, bad, encounters, bench)
            raise InvalidRateStop(f"invalid rate above threshold in generation {gen}: {bad}")
        return summary

    def invalid_rates(self, encounters, bench) -> dict:
        out = {}
        for p in self.pops:
            n = bad = refusals = 0
            reasons: dict[str, int] = {}
            for e in encounters:
                if e["pop"] != p:
                    continue
                for side in ("a", "b"):
                    s = e[side]
                    n += 2
                    bad += (not s["valid_declare"]) + (not s["valid_action"])
                    for r in s["invalid_reasons"]:
                        reasons[r] = reasons.get(r, 0) + 1
                    refusals += sum(r == "refusal" for r in s["invalid_reasons"])
            for b in bench:
                if b["pop"] != p:
                    continue
                for r in b["encounters"]:
                    n += 2
                    bad += (not r["valid_declare"]) + (not r["valid_action"])
                    for x in r["invalid_reasons"]:
                        reasons[x] = reasons.get(x, 0) + 1
                    refusals += sum(x == "refusal" for x in r["invalid_reasons"])
            out[p] = {"n": n, "invalid": bad, "rate": bad / max(1, n), "refusals": refusals, "reasons": reasons}
        return out

    def persist_generation(self, gen, encounters, bench, gen_genomes, mutations, summary):
        d = self.out
        _write_jsonl_gz(d / "encounters.jsonl.gz", encounters)
        _write_jsonl_gz(d / "benchmark.jsonl.gz", bench)
        _write_jsonl_gz(d / "mutations.jsonl.gz", mutations)
        gdir = d / "genomes"
        gdir.mkdir(parents=True, exist_ok=True)
        (gdir / f"gen-{gen:02d}.json").write_text(json.dumps(gen_genomes, ensure_ascii=False, indent=0))
        with open(d / "generations.jsonl", "a") as f:
            f.write(json.dumps(summary) + "\n")
        _write_jsonl_gz(self.log_path, self.gw.log.drain())
        self.gw.budget.save()
        self.next_gen = gen + 1
        self.save_checkpoint()

    def write_diagnosis(self, gen, bad, encounters, bench):
        lines = [f"# Diagnosis: invalid-rate stop (seed {self.seed}, generation {gen}, phase {self.tag})", "",
                 f"Threshold: {self.cfg['game']['invalid_rate_stop']:.0%} invalid player outputs per population and generation.",
                 ""]
        for p, v in bad.items():
            lines.append(f"## {p}: {v['invalid']}/{v['n']} = {v['rate']:.1%} invalid, {v['refusals']} refusals")
            lines.append("")
            lines.append("Reasons: " + ", ".join(f"{k}: {c}" for k, c in sorted(v["reasons"].items(), key=lambda t: -t[1])))
            lines.append("")
        lines.append("Raw responses of invalid calls are in the call log (fields `response_text`, `stop_reason`, `error`).")
        (self.out / f"DIAGNOSIS-gen{gen:02d}.md").write_text("\n".join(lines) + "\n")

    async def run(self, resume: bool = True, max_gens: int | None = None) -> list[dict]:
        if not (resume and self.load_checkpoint()):
            self.init_state()
        summaries = []
        stop = self.n_gens if max_gens is None else min(self.n_gens, self.next_gen + max_gens)
        for gen in range(self.next_gen, stop):
            summaries.append(await self.run_generation(gen))
        return summaries
