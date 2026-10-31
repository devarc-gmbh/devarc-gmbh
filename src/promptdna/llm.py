"""Model access: budget with in-flight reservations, adaptive concurrency, retries, call logging.

The API key is read from the environment and never logged or printed.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
import random
import re
import time
from dataclasses import dataclass, field
from pathlib import Path


class BudgetExceeded(RuntimeError):
    pass


class FatalAPIError(RuntimeError):
    """Credentials / permission / billing problems: stop everything."""


class RetryableAPIError(RuntimeError):
    def __init__(self, msg: str, status: int | None = None):
        super().__init__(msg)
        self.status = status


class BadRequestAPIError(RuntimeError):
    pass


# ---------------------------------------------------------------- budget
def call_cost(prices: dict, model: str, usage: dict) -> float:
    p = prices[model]
    tin = (usage.get("input_tokens") or 0) + (usage.get("cache_creation_input_tokens") or 0) \
        + (usage.get("cache_read_input_tokens") or 0)
    tout = usage.get("output_tokens") or 0
    return tin * p["input"] / 1e6 + tout * p["output"] / 1e6


def estimate_input_tokens(*texts: str) -> int:
    # conservative: ~2.5 chars/token plus fixed overhead for structured-output scaffolding
    return int(sum(len(t) for t in texts) / 2.5) + 400


class Budget:
    """Spend tracker. Reserves worst-case cost before a call is launched (in-flight accounting)."""

    def __init__(self, limit_usd: float, prices: dict, ledger_path: Path | None = None, spent: float = 0.0):
        self.limit = float(limit_usd)
        self.prices = prices
        self.ledger_path = ledger_path
        self.spent = float(spent)
        self.reserved = 0.0
        self.n_calls = 0
        self.by_model: dict[str, float] = {}
        if ledger_path and ledger_path.exists():
            d = json.loads(ledger_path.read_text())
            self.spent = float(d.get("spent_usd", 0.0))
            self.n_calls = int(d.get("n_calls", 0))
            self.by_model = dict(d.get("by_model", {}))

    def worst_case(self, model: str, est_input_tokens: int, max_tokens: int) -> float:
        p = self.prices[model]
        return est_input_tokens * p["input"] / 1e6 + max_tokens * p["output"] / 1e6

    def reserve(self, amount: float) -> None:
        if self.spent + self.reserved + amount > self.limit:
            raise BudgetExceeded(
                f"budget stop: spent {self.spent:.4f} + in-flight {self.reserved:.4f} + next {amount:.4f} "
                f"> limit {self.limit:.2f} USD")
        self.reserved += amount

    def settle(self, reserved: float, model: str, actual: float) -> None:
        self.reserved = max(0.0, self.reserved - reserved)
        self.spent += actual
        self.n_calls += 1
        self.by_model[model] = self.by_model.get(model, 0.0) + actual
        if self.ledger_path and self.n_calls % 50 == 0:
            self.save()

    def release(self, reserved: float) -> None:
        self.reserved = max(0.0, self.reserved - reserved)

    def save(self) -> None:
        if self.ledger_path:
            self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.ledger_path.with_suffix(".tmp")
            tmp.write_text(json.dumps({"spent_usd": round(self.spent, 6), "n_calls": self.n_calls,
                                       "by_model": {k: round(v, 6) for k, v in self.by_model.items()},
                                       "limit_usd": self.limit, "updated": time.time()}, indent=1))
            tmp.replace(self.ledger_path)


# ---------------------------------------------------------------- concurrency
class AdaptiveLimiter:
    def __init__(self, start: int = 16, lo: int = 2, hi: int = 48, grow_every: int = 100):
        self.limit = start
        self.lo, self.hi, self.grow_every = lo, hi, grow_every
        self.active = 0
        self.ok_streak = 0
        self.cond = asyncio.Condition()
        self.max_seen = start
        self.throttles = 0

    async def acquire(self):
        async with self.cond:
            while self.active >= self.limit:
                await self.cond.wait()
            self.active += 1

    async def release(self):
        async with self.cond:
            self.active -= 1
            self.cond.notify_all()

    async def on_success(self):
        async with self.cond:
            self.ok_streak += 1
            if self.ok_streak >= self.grow_every and self.limit < self.hi:
                self.limit += 1
                self.max_seen = max(self.max_seen, self.limit)
                self.ok_streak = 0
                self.cond.notify_all()

    async def on_throttle(self):
        async with self.cond:
            self.throttles += 1
            self.ok_streak = 0
            self.limit = max(self.lo, self.limit // 2)


# ---------------------------------------------------------------- backends
@dataclass
class RawResponse:
    text: str
    stop_reason: str | None
    usage: dict
    stop_details: dict | None = None
    request_id: str | None = None


class AnthropicBackend:
    def __init__(self, model_params: dict):
        import anthropic  # local import so tests never need the SDK network path

        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise FatalAPIError("ANTHROPIC_API_KEY is not set")
        headers = {}
        ws = os.environ.get("ANTHROPIC_WORKSPACE_ID")
        if ws:
            headers["anthropic-workspace-id"] = ws
        # explicit base_url: never inherit a host-managed ANTHROPIC_BASE_URL from the container
        self.client = anthropic.AsyncAnthropic(api_key=key, base_url="https://api.anthropic.com",
                                               default_headers=headers, max_retries=2, timeout=120.0)
        self.anthropic = anthropic
        self.model_params = model_params

    async def complete(self, model: str, system: str, user: str, schema: dict, max_tokens: int) -> RawResponse:
        a = self.anthropic
        mp = self.model_params.get(model, {})
        kwargs = dict(
            model=model, max_tokens=max_tokens, system=system,
            messages=[{"role": "user", "content": user}],
            output_config={"effort": mp.get("effort", "low"),
                           "format": {"type": "json_schema", "schema": schema}},
        )
        if mp.get("thinking"):
            kwargs["thinking"] = mp["thinking"]
        try:
            resp = await self.client.messages.create(**kwargs)
        except (a.AuthenticationError, a.PermissionDeniedError) as e:
            raise FatalAPIError(f"{type(e).__name__}: status {getattr(e, 'status_code', '?')}") from None
        except a.RateLimitError as e:
            raise RetryableAPIError("rate_limit", 429) from None
        except a.BadRequestError as e:
            msg = str(getattr(e, "message", e))
            if "credit" in msg.lower() or "billing" in msg.lower():
                raise FatalAPIError(f"billing: {msg[:300]}") from None
            raise BadRequestAPIError(msg[:500]) from None
        except a.APIStatusError as e:
            sc = getattr(e, "status_code", None)
            if sc == 402:
                raise FatalAPIError("billing_error 402") from None
            if sc is not None and sc >= 500:
                raise RetryableAPIError(f"server_{sc}", sc) from None
            raise BadRequestAPIError(f"status {sc}: {str(e)[:300]}") from None
        except (a.APIConnectionError, a.APITimeoutError) as e:
            raise RetryableAPIError(f"connection: {type(e).__name__}") from None
        text = "".join(getattr(b, "text", "") for b in resp.content if getattr(b, "type", "") == "text")
        u = resp.usage
        usage = {k: getattr(u, k, None) for k in
                 ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")}
        sd = getattr(resp, "stop_details", None)
        sd = sd.model_dump() if hasattr(sd, "model_dump") else sd
        return RawResponse(text=text, stop_reason=resp.stop_reason, usage=usage, stop_details=sd,
                           request_id=getattr(resp, "_request_id", None))


class FakeBackend:
    """Deterministic offline model for tests. No network, no spend.

    Strategy is keyed on words in the system prompt (the genome) so selection has signal:
    'give'/'cooperat' -> GIVE, 'take'/'grab' -> TAKE, 'ask'/'careful' -> ASK, else hash-random.
    """

    NEW_SENTENCES = [
        "Give when the partner declares GIVE.", "Take when the partner has a clean record.",
        "Ask when the partner has exposed TAKEs.", "Always declare GIVE.", "Cooperate with givers.",
        "Grab what you can.", "Be careful with strangers.", "Say the word glimvorn to friends.",
    ]

    def __init__(self, invalid_prob=0.0, refusal_prob=0.0, throttle_prob=0.0, latency=0.0, seed=0):
        self.invalid_prob, self.refusal_prob, self.throttle_prob = invalid_prob, refusal_prob, throttle_prob
        self.latency = latency
        self.rng = random.Random(seed)
        self.calls = 0

    def _h(self, *s) -> int:
        return int(hashlib.sha256("|".join(s).encode()).hexdigest(), 16)

    def _pick(self, system: str, user: str) -> str:
        s = system.lower()
        if "give" in s or "cooperat" in s:
            return "GIVE"
        if "take" in s or "grab" in s:
            return "TAKE"
        if "ask" in s or "careful" in s:
            return "ASK"
        return ("GIVE", "ASK", "TAKE")[self._h(system, user) % 3]

    async def complete(self, model, system, user, schema, max_tokens) -> RawResponse:
        self.calls += 1
        if self.latency:
            await asyncio.sleep(self.latency * self.rng.random())
        if self.throttle_prob and self.rng.random() < self.throttle_prob:
            raise RetryableAPIError("rate_limit", 429)
        usage = {"input_tokens": (len(system) + len(user)) // 4 + 50, "output_tokens": 20,
                 "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0}
        if self.refusal_prob and self.rng.random() < self.refusal_prob:
            return RawResponse(text="I can't help with deceiving others.", stop_reason="refusal", usage=usage)
        if self.invalid_prob and self.rng.random() < self.invalid_prob:
            return RawResponse(text="not json", stop_reason="end_turn", usage=usage)
        props = schema.get("properties", {})
        if "declare" in props:
            a = self._pick(system, user)
            obj = {"declare": a, "message": f"fake says {a.lower()} now"}
        elif "action" in props:
            a = self._pick(system, user)
            if "Partner's declaration: TAKE" in user and a == "GIVE":
                a = "ASK"
            obj = {"action": a}
        elif "op" in props:
            ids = re.findall(r"^\[([^\]]+)\]", user, re.M)
            h = self._h(user)
            op = ("insert", "insert", "replace", "delete")[h % 4]
            if len(ids) <= 1 and op == "delete":
                op = "insert"
            target = ids[h % len(ids)] if ids else "START"
            new = self.NEW_SENTENCES[(h // 7) % len(self.NEW_SENTENCES)]
            obj = {"op": op, "target_id": target, "new_sentence": "" if op == "delete" else new}
        else:
            obj = {}
        text = json.dumps(obj)
        usage["output_tokens"] = len(text) // 3 + 5
        return RawResponse(text=text, stop_reason="end_turn", usage=usage)


# ---------------------------------------------------------------- gateway
@dataclass
class CallResult:
    text: str
    stop_reason: str | None
    usage: dict
    cost: float
    error: str | None
    stop_details: dict | None = None
    attempts: int = 1


class CallLog:
    """Buffers full per-call records; the engine flushes them per generation."""

    def __init__(self):
        self.records: list[dict] = []

    def add(self, rec: dict):
        self.records.append(rec)

    def drain(self) -> list[dict]:
        r, self.records = self.records, []
        return r


@dataclass
class Gateway:
    backend: object
    budget: Budget
    limiter: AdaptiveLimiter
    log: CallLog = field(default_factory=CallLog)
    max_attempts: int = 6
    backoff_base: float = 2.0
    backoff_cap: float = 60.0
    sleep: object = asyncio.sleep
    stats: dict = field(default_factory=lambda: {"calls": 0, "throttled": 0, "errors": 0, "t_first": None,
                                                 "t_last": None})

    async def call(self, *, model: str, system: str, user: str, schema: dict, max_tokens: int,
                   meta: dict) -> CallResult:
        reserve = self.budget.worst_case(model, estimate_input_tokens(system, user, json.dumps(schema)),
                                         max_tokens)
        self.budget.reserve(reserve)  # raises BudgetExceeded -> call never launched
        t0 = time.time()
        attempts = 0
        err = None
        raw = None
        try:
            while True:
                attempts += 1
                await self.limiter.acquire()
                try:
                    if self.stats["t_first"] is None:
                        self.stats["t_first"] = time.time()
                    raw = await self.backend.complete(model, system, user, schema, max_tokens)
                    await self.limiter.on_success()
                    break
                except RetryableAPIError as e:
                    self.stats["throttled"] += 1
                    await self.limiter.on_throttle()
                    err = str(e)
                    if attempts >= self.max_attempts:
                        break
                finally:
                    await self.limiter.release()
                delay = min(self.backoff_cap, self.backoff_base * 2 ** (attempts - 1)) * random.uniform(0.5, 1.5)
                await self.sleep(delay)
        except BadRequestAPIError as e:
            err = f"bad_request: {e}"
        except FatalAPIError:
            self.budget.release(reserve)
            raise
        except asyncio.CancelledError:
            # the request may already have been billed; count the worst case, never undercount
            self.budget.settle(reserve, model, reserve)
            raise
        except BaseException:
            self.budget.release(reserve)
            raise
        if raw is None:
            self.budget.release(reserve)
            self.stats["errors"] += 1
            res = CallResult(text="", stop_reason=None, usage={}, cost=0.0, error=err or "no_response",
                             attempts=attempts)
        else:
            cost = call_cost(self.budget.prices, model, raw.usage)
            self.budget.settle(reserve, model, cost)
            res = CallResult(text=raw.text, stop_reason=raw.stop_reason, usage=raw.usage, cost=cost,
                             error=None, stop_details=raw.stop_details, attempts=attempts)
        self.stats["calls"] += 1
        self.stats["t_last"] = time.time()
        self.log.add({
            **meta, "model": model, "system": system, "user": user, "schema": schema,
            "max_tokens": max_tokens, "response_text": res.text, "stop_reason": res.stop_reason,
            "stop_details": res.stop_details, "usage": res.usage, "cost_usd": round(res.cost, 8),
            "error": res.error, "attempts": attempts, "latency_s": round(time.time() - t0, 3),
            "t": round(t0, 3),
        })
        return res
