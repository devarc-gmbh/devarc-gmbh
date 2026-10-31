"""Genome = ordered list of sentences, each with a stable ID and provenance."""
from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def split_sentences(text: str) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    return [s for s in _SENT_SPLIT.split(text) if s]


def word_count(text: str) -> int:
    return len(text.split())


@dataclass
class Sentence:
    id: str
    text: str
    origin_genome: str | None  # genome id in which this sentence was created
    origin_gen: int
    origin_pop: str
    op: str  # "root" | "insert" | "replace"
    replaced_from: str | None = None  # sentence id this one replaced (family lineage)
    truncated: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: dict) -> "Sentence":
        return Sentence(**d)


@dataclass
class Genome:
    id: str
    sentences: list[Sentence]
    parent_id: str | None
    gen: int
    pop: str
    edit: dict | None = None  # description of the single edit that created it
    flags: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return " ".join(s.text for s in self.sentences)

    @property
    def n_words(self) -> int:
        return word_count(self.text)

    def numbered(self) -> str:
        return "\n".join(f"[{s.id}] {s.text}" for s in self.sentences)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "parent_id": self.parent_id,
            "gen": self.gen,
            "pop": self.pop,
            "text": self.text,
            "n_words": self.n_words,
            "edit": self.edit,
            "flags": list(self.flags),
            "sentences": [s.to_dict() for s in self.sentences],
        }

    @staticmethod
    def from_dict(d: dict) -> "Genome":
        return Genome(
            id=d["id"],
            sentences=[Sentence.from_dict(s) for s in d["sentences"]],
            parent_id=d["parent_id"],
            gen=d["gen"],
            pop=d["pop"],
            edit=d.get("edit"),
            flags=list(d.get("flags", [])),
        )


class IdFactory:
    """Deterministic, collision-free IDs per seed/population."""

    def __init__(self, prefix: str, counters: dict | None = None):
        self.prefix = prefix
        self.counters = dict(counters or {"g": 0, "s": 0, "a": 0})

    def _next(self, kind: str) -> str:
        self.counters[kind] += 1
        return f"{self.prefix}-{kind}{self.counters[kind]:05d}"

    def genome(self) -> str:
        return self._next("g")

    def sentence(self) -> str:
        return self._next("s")

    def agent(self) -> str:
        return self._next("a")


def root_genome(text: str, pop: str, ids: IdFactory) -> Genome:
    gid = ids.genome()
    sents = [
        Sentence(id=ids.sentence(), text=t, origin_genome=gid, origin_gen=0, origin_pop=pop, op="root")
        for t in split_sentences(text)
    ]
    return Genome(id=gid, sentences=sents, parent_id=None, gen=0, pop=pop, edit={"op": "root"})


def clone_genome(parent: Genome, gen: int, ids: IdFactory) -> Genome:
    return Genome(
        id=ids.genome(),
        sentences=[Sentence(**s.to_dict()) for s in parent.sentences],
        parent_id=parent.id,
        gen=gen,
        pop=parent.pop,
        edit={"op": "clone"},
    )


def normalize_new_sentence(raw: str, word_cap: int) -> tuple[str, list[str]]:
    """Force mutator output to exactly one sentence of <= word_cap words."""
    flags: list[str] = []
    parts = split_sentences(raw or "")
    if not parts:
        return "", ["empty_sentence"]
    s = parts[0]
    if len(parts) > 1:
        flags.append("multi_sentence_trimmed")
    words = s.split()
    if len(words) > word_cap:
        s = " ".join(words[:word_cap])
        flags.append("sentence_word_cap")
    if s[-1] not in ".!?":
        s += "."
    return s, flags


class EditError(ValueError):
    pass


def apply_edit(parent: Genome, op: str, target_id: str, new_text: str, gen: int,
               ids: IdFactory, word_cap: int, sentence_word_cap: int) -> Genome:
    """Apply exactly one sentence-level edit; raise EditError if structurally invalid."""
    op = (op or "").strip().lower()
    target_id = (target_id or "").strip().strip("[]")
    sents = [Sentence(**s.to_dict()) for s in parent.sentences]
    index = {s.id: i for i, s in enumerate(sents)}
    flags: list[str] = []
    # child id is only allocated once the edit is known to be valid

    if op == "delete":
        if target_id not in index:
            raise EditError(f"delete: unknown target {target_id!r}")
        if len(sents) <= 1:
            raise EditError("delete: cannot delete the only sentence")
        removed = sents.pop(index[target_id])
        edit = {"op": "delete", "target_id": target_id, "old_text": removed.text}
        child_id = ids.genome()
    elif op in ("insert", "replace"):
        text, nflags = normalize_new_sentence(new_text, sentence_word_cap)
        flags += nflags
        if not text:
            raise EditError(f"{op}: empty new sentence")
        if op == "replace":
            if target_id not in index:
                raise EditError(f"replace: unknown target {target_id!r}")
            i = index[target_id]
            if sents[i].text == text:
                raise EditError("replace: new sentence identical to old")
            child_id = ids.genome()
            old = sents[i]
            sents[i] = Sentence(id=ids.sentence(), text=text, origin_genome=child_id, origin_gen=gen,
                                origin_pop=parent.pop, op="replace", replaced_from=old.id)
            edit = {"op": "replace", "target_id": target_id, "old_text": old.text, "new_text": text,
                    "new_id": sents[i].id}
        else:
            if target_id.upper() == "START":
                pos = 0
            elif target_id in index:
                pos = index[target_id] + 1
            else:
                raise EditError(f"insert: unknown anchor {target_id!r}")
            child_id = ids.genome()
            ns = Sentence(id=ids.sentence(), text=text, origin_genome=child_id, origin_gen=gen,
                          origin_pop=parent.pop, op="insert")
            sents.insert(pos, ns)
            edit = {"op": "insert", "target_id": target_id, "new_text": text, "new_id": ns.id}
    else:
        raise EditError(f"unknown op {op!r}")

    sents, tflags = truncate_sentences(sents, word_cap)
    flags += tflags
    return Genome(id=child_id, sentences=sents, parent_id=parent.id, gen=gen, pop=parent.pop,
                  edit=edit, flags=flags)


def truncate_sentences(sents: list[Sentence], word_cap: int) -> tuple[list[Sentence], list[str]]:
    """Hard-truncate genome to word_cap words (cut mid-sentence if needed)."""
    out: list[Sentence] = []
    total = 0
    for s in sents:
        w = s.text.split()
        if total + len(w) <= word_cap:
            out.append(s)
            total += len(w)
            continue
        room = word_cap - total
        if room > 0:
            cut = Sentence(**s.to_dict())
            cut.text = " ".join(w[:room])
            cut.truncated = True
            out.append(cut)
        return out, ["genome_truncated"]
    return out, []
