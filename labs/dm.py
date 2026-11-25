"""Helpers shared by the labs of Discrete Mathematics and Logic for Computing (FND-MTH-105).

    import dm as U

- U.QUICK is True when the environment variable DM_QUICK is 1: smaller enumerations.
- U.pick(full, quick) returns the small value in quick mode.
- U.load_csv(name) reads labs/data/<name> as a list of dictionaries of strings.
- U.load_json(name) reads labs/data/<name>.
- U.pairs(name, a, b) reads two columns of a CSV file as a set of pairs: a relation.
- U.reference(name) reads labs/data/reference/<name>.json, the safety net of an exercise.
- U.keep(name, value) returns value; with DM_WRITE_REF=1 (the trainer's tool) it also saves it.
- U.check(condition, message) prints a tick or raises AssertionError.
- U.table(rows, header) prints a small table without any extra library.
"""
from __future__ import annotations

import csv
import json
import os
from pathlib import Path

LABS = Path(__file__).resolve().parent
DATA = LABS / "data"
REF = DATA / "reference"
QUICK = os.environ.get("DM_QUICK", "0") == "1"


def pick(full, quick):
    """The full value, or the small one in quick mode."""
    return quick if QUICK else full


def load_csv(name: str) -> list[dict]:
    with (DATA / name).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_json(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def pairs(name: str, a: str, b: str) -> set[tuple[str, str]]:
    """Two columns of a CSV file as a set of ordered pairs."""
    return {(r[a], r[b]) for r in load_csv(name)}


def _plain(obj):
    if isinstance(obj, (set, frozenset)):
        return sorted(_plain(x) for x in obj)
    if isinstance(obj, tuple):
        return [_plain(x) for x in obj]
    if isinstance(obj, list):
        return [_plain(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): _plain(v) for k, v in obj.items()}
    if isinstance(obj, float):
        return round(obj, 6)
    return obj


def reference(name: str):
    """The reference result of an exercise, for the safety net."""
    return json.loads((REF / f"{name}.json").read_text(encoding="utf-8"))


def keep(name: str, value):
    """Return value; when DM_WRITE_REF=1 (the trainer's tool), also save it as a reference file."""
    if os.environ.get("DM_WRITE_REF") == "1":
        REF.mkdir(parents=True, exist_ok=True)
        (REF / f"{name}.json").write_text(json.dumps(_plain(value), indent=1) + "\n", encoding="utf-8", newline="\n")
    return value


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError("not yet: " + message)
    print("[ok]", message)


def table(rows, header) -> None:
    """Print rows as a plain table."""
    rows = [[str(x) for x in r] for r in rows]
    widths = [max(len(str(h)), *(len(r[i]) for r in rows)) if rows else len(str(h)) for i, h in enumerate(header)]
    print("  ".join(str(h).ljust(w) for h, w in zip(header, widths)))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print("  ".join(x.ljust(w) for x, w in zip(r, widths)))
