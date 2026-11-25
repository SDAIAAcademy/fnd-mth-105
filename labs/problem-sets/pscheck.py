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


# ---------------------------------------------------------------- PS2 truth tables
def _imp(a, b):
    return (not a) or b


def _ps2(ns):
    def taut_ok():
        f = ns["is_tautology"]
        yes = [(lambda p: p or not p, 1), (lambda p, q: _imp(p and q, p), 2),
               (lambda p, q, r: _imp(_imp(p, q) and _imp(q, r), _imp(p, r)), 3)]
        no = [(lambda p, q: _imp(p, q), 2), (lambda p: p and not p, 1), (lambda p, q: _imp(p or q, p), 2)]
        return all(f(g, n) is True or f(g, n) == True for g, n in yes) and all(not f(g, n) for g, n in no)  # noqa: E712
    yield "2 is_tautology: three tautologies and three formulas that are not", _run(taut_ok)

    def models_ok():
        f = ns["count_models"]
        for n in range(1, 7):
            if f(lambda *r: any(r), n) != 2 ** n - 1 or f(lambda *r: all(r), n) != 1:
                return False
            if f(lambda *r: sum(r) % 2 == 1, n) != 2 ** (n - 1) or f(lambda *r: False, n) != 0:
                return False
        return True
    yield "4 count_models: or, and, odd parity and false on one to six variables", _run(models_ok)


# ---------------------------------------------------------------- PS3 relations
def _ps3(ns):
    def sym_ok():
        f = ns["symmetric_closure"]
        for _ in range(20):
            X = range(6)
            R = {(RNG.choice(X), RNG.choice(X)) for _ in range(RNG.randrange(0, 12))}
            S = set(f(R))
            if not R <= S or any((y, x) not in S for x, y in S):
                return False
            if any((x, y) not in R and (y, x) not in R for x, y in S):
                return False
        return True
    yield "2 symmetric_closure: contains R, symmetric, nothing extra", _run(sym_ok)

    def wit_ok():
        f = ns["transitivity_witness"]
        for _ in range(20):
            xs = RNG.sample(range(50), 6)
            le = {(a, b) for a in xs for b in xs if a <= b}
            if f(le) is not None:
                return False
            a, b, c = RNG.sample(range(100, 200), 3)
            R = {(a, b), (b, c)} | {(RNG.randrange(300, 310), RNG.randrange(300, 310)) for _ in range(3)}
            R = {p for p in R if p != (a, c)}
            w = f(R)
            if w is None:
                return False
            x, y, z = w
            if (x, y) not in R or (y, z) not in R or (x, z) in R:
                return False
        return True
    yield "5 transitivity_witness: None for an order, a real witness otherwise", _run(wit_ok)


# ---------------------------------------------------------------- PS4 induction and invariants
def _ps4(ns):
    def max_ok():
        f = ns["running_max"]
        for n in (1, 2, 7, 30):
            xs = [RNG.randrange(-100, 100) for _ in range(n)]
            if f(list(xs)) != max(xs):
                return False
        return True
    yield "2 running_max: the largest element, on generated lists", _run(max_ok)

    def tree(h):
        """A tree of height exactly h, with random extra branches that are not taller."""
        if h == 0:
            return {"code": "leaf", "children": []}
        kids = [tree(h - 1)] + [tree(RNG.randrange(0, h)) for _ in range(RNG.randrange(0, 3))]
        RNG.shuffle(kids)
        return {"code": "node", "children": kids}

    def height_ok():
        f = ns["height"]
        return all(f(tree(h)) == h for h in (0, 1, 2, 4, 6))
    yield "5 height: trees built with a known height", _run(height_ok)


# ---------------------------------------------------------------- PS5 counting
def _ps5(ns):
    import math

    def pc_ok():
        perm, comb = ns["perm"], ns["comb"]
        for n in range(0, 12):
            for k in range(0, n + 1):
                if perm(n, k) != math.perm(n, k) or comb(n, k) != math.comb(n, k):
                    return False
        return True
    yield "2 perm and comb: agree with the library for n up to 11", _run(pc_ok)

    def onto_ok():
        f = ns["count_onto"]
        for n in range(1, 7):
            for k in range(1, 5):
                expect = sum((-1) ** i * math.comb(k, i) * (k - i) ** n for i in range(k + 1))
                if f(n, k) != expect:
                    return False
        return True
    yield "5 count_onto: agrees with inclusion-exclusion for small sizes", _run(onto_ok)


# ---------------------------------------------------------------- PS6 inclusion-exclusion
def _ps6(ns):
    def union_ok():
        f = ns["union_size"]
        for k in range(1, 6):
            sets = [set(RNG.sample(range(30), RNG.randrange(0, 15))) for _ in range(k)]
            if f(sets) != len(set().union(*sets)):
                return False
        return True
    yield "2 union_size: agrees with the size of the union", _run(union_ok)

    def small_ok():
        f = ns["smallest_group"]
        from collections import Counter
        for _ in range(10):
            rows = [{"a": RNG.choice("xy"), "b": RNG.choice("pqr"), "c": RNG.randrange(3)} for _ in range(40)]
            for keys in (["a"], ["a", "b"], ["a", "b", "c"]):
                if f(rows, keys) != min(Counter(tuple(r[k] for k in keys) for r in rows).values()):
                    return False
        return True
    yield "5 smallest_group: on generated rows and key lists", _run(small_ok)


# ---------------------------------------------------------------- PS7 recurrences and graphs
def _ps7(ns):
    import math
    import time

    def orders_ok():
        f = ns["count_orders"]
        if f(list("abcde"), []) != 120:
            return False
        if f(list("abcd"), [("a", "b"), ("b", "c"), ("c", "d")]) != 1:
            return False
        nodes = ["p1", "p2", "p3", "q1", "q2"]
        return f(nodes, [("p1", "p2"), ("p2", "p3"), ("q1", "q2")]) == math.comb(5, 2)
    yield "2 count_orders: no edges, a chain, and two chains side by side", _run(orders_ok)

    def stair_ok():
        f = ns["stair_ways"]
        t0 = time.perf_counter()
        vals = [f(n) for n in range(1, 81)]
        fast = time.perf_counter() - t0 < 2
        return vals[0] == 1 and vals[1] == 2 and all(vals[i] == vals[i - 1] + vals[i - 2] for i in range(2, 80)) and fast
    yield "5 stair_ways: first values, the recurrence up to 80, and fast", _run(stair_ok)


def check(n: int, ns: dict) -> None:
    items = list(globals()[f"_ps{n}"](ns))
    score = 0
    for label, (ok, why) in items:
        score += ok
        print(("[ok]   " if ok else "[not yet] ") + label + ("" if ok else f": {why}"))
    print(f"code items: {score} of {len(items)}")
    for w in WRITTEN[n]:
        print(f"[trainer] {w}: marked by the trainer")
