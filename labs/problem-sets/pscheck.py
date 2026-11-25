"""The checker of the code items of the weekly problem sets (PS1 to PS7).

The last cell of each problem-set notebook calls `pscheck.check(n, globals())`. It prints one
line per code item and lists the written items, which the trainer marks. It stores no answers:
every case it runs is generated so that the right result is known by construction (a map built
as a bijection, a formula built to be true on every row), or it checks a property any right
answer must have (the right size, no repeats, every rule met).

A function that is not written yet scores nothing; a function that raises an error is reported
with the error, not as a crash.
"""
from __future__ import annotations

import itertools
import random

RNG = random.Random(2027)
WRITTEN = {
    1: ["1 a set identity", "4 which kind of function", "5 inverse of a composition"],
    2: ["1 translate three access rules", "3 valid or invalid", "5 an encoding in words"],
    3: ["1 quantifiers and negation", "3 a direct proof", "4 a proof by contradiction"],
    4: ["1 an induction proof with its test", "3 a loop invariant", "4 the gap in a proof"],
    5: ["1 counting codes", "3 a pigeonhole argument", "4 a collision formula explained"],
    6: ["1 inclusion-exclusion by hand", "3 a linkage count", "4 a note on anonymisation"],
    7: ["1 a recurrence solved and proved", "3 a topological order by hand", "4 growth compared"],
}


def _run(test):
    try:
        ok = bool(test())
        return ok, "" if ok else "wrong on a generated case"
    except NotImplementedError:
        return False, "not written yet"
    except Exception as e:  # noqa: BLE001 - a learner's error is a result, not a crash
        return False, f"{type(e).__name__}: {e}"


# ---------------------------------------------------------------- PS1 sets, functions, composition
def _ps1(ns):
    def power_set_ok():
        f = ns["power_set"]
        for n in range(0, 6):
            S = set(RNG.sample(range(100), n))
            P = f(S)
            if len(P) != 2 ** n or len(set(map(frozenset, P))) != 2 ** n:
                return False
            if not all(set(x) <= S for x in P):
                return False
        return True
    yield "2 power_set: right size, no repeats, only subsets", _run(power_set_ok)

    def compose_ok():
        f = ns["compose_maps"]
        for n in (1, 4, 9):
            X = list(range(n))
            ys = RNG.sample(range(100, 200), n)
            zs = RNG.sample(range(300, 400), n)
            fx = dict(zip(X, ys))
            gy = dict(zip(ys, zs))
            if f(fx, gy) != dict(zip(X, zs)):
                return False
        return True
    yield "3 compose_maps: f then g on generated maps", _run(compose_ok)


def check(n: int, ns: dict) -> None:
    items = list(globals()[f"_ps{n}"](ns))
    score = 0
    for label, (ok, why) in items:
        score += ok
        print(("[ok]   " if ok else "[not yet] ") + label + ("" if ok else f": {why}"))
    print(f"code items: {score} of {len(items)}")
    for w in WRITTEN[n]:
        print(f"[trainer] {w}: marked by the trainer")
