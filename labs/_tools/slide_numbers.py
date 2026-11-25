"""Recompute every number the slides quote from their parallel examples (not the labs' data).

    uv run python _tools/slide_numbers.py        (from labs/)

The labs' own numbers come from running the solution notebooks; the debrief slides quote those.
"""
import itertools
import math
from fractions import Fraction


def p_shared(N, n):
    """Exact chance that n values drawn uniformly from N are not all different."""
    p = Fraction(1)
    for i in range(n):
        p *= Fraction(N - i, N)
    return 1 - p


def week5():
    print("== week 5")
    print("plates, 3 letters then 4 digits:", f"{26 ** 3 * 10 ** 4:,}")
    print("PINs of 4, 5 or 6 digits:", f"{10 ** 4 + 10 ** 5 + 10 ** 6:,}")
    print("committee of 3 from 8:", math.comb(8, 3), "| ordered roles:", math.perm(8, 3))
    n = 1
    while p_shared(100, n) <= Fraction(1, 2):
        n += 1
    print("100 locker codes: smallest n with a shared code more likely than not:", n,
          f"| chance {float(p_shared(100, n)):.4f} | 1.18 * sqrt(100) = {1.18 * 10:.1f}")
    print("chance of a shared code, 100 codes, n = 5, 10, 20:", [round(float(p_shared(100, k)), 4) for k in (5, 10, 20)])
    print("expected colliding pairs, 30 people, 100 codes:", math.comb(30, 2) / 100)
    print("pigeonhole, 1,000 people over 366 possible birthdays: at least", -(-1000 // 366))
    # brute force check of the 100-code chance is too big; check the formula on 6 codes, 3 people
    brute = sum(1 for a in itertools.product(range(6), repeat=3) if len(set(a)) == 3)
    print("6 codes, 3 people: all different", brute, "of", 6 ** 3, "=", Fraction(brute, 6 ** 3), "| formula", 1 - p_shared(6, 3))


def week6():
    print("== week 6")
    # a parallel town: 20,000 adults, birth dates over 60 years, 2 sexes, 10 districts
    days = 60 * 365
    for name, cells in [("birth date, sex, district", days * 2 * 10), ("birth year, sex, district", 60 * 2 * 10),
                        ("10-year band, sex, district", 6 * 2 * 10)]:
        n = 20000
        unique = n * (1 - 1 / cells) ** (n - 1)
        print(f"{name}: {cells:,} combinations, {n / cells:.2f} people each on average; "
              f"expected unique if uniform {unique:,.0f} ({unique / n:.1%})")
    # inclusion-exclusion on a small example
    A, B = set(range(0, 60)), set(range(40, 90))
    print("|A| =", len(A), "|B| =", len(B), "|A and B| =", len(A & B), "|A or B| =", len(A | B))
    a, b, c, ab, ac, bc, abc = 120, 90, 60, 30, 20, 15, 5
    print("three sets:", a + b + c - ab - ac - bc + abc)


def week7():
    print("== week 7")
    # monotone paths in an n by n grid, moving right or down: C(2n, n)
    for n in (5, 10, 20, 30):
        print("grid", n, "x", n, "monotone paths:", f"{math.comb(2 * n, n):,}")
    print("n^2, 2^n, n! at n = 10, 20, 30:", [(n, n * n, f"{2 ** n:,}", f"{math.factorial(n):.2e}") for n in (10, 20, 30)])
    # a small DAG for the slides, a parallel to the pipeline (not the lab's diamond)
    edges = [("A", "C"), ("B", "C"), ("C", "D"), ("C", "E")]
    import networkx as nx
    orders = sorted(nx.all_topological_sorts(nx.DiGraph(edges)))
    print("small DAG A->C, B->C, C->D, C->E: topological orders", len(orders), [''.join(o) for o in orders])
    # paths into each point of a 3 by 3 grid of points by the recurrence P(i, j) = P(i-1, j) + P(i, j-1)
    P = {}
    for i in range(3):
        for j in range(3):
            P[i, j] = 1 if i == 0 or j == 0 else P[i - 1, j] + P[i, j - 1]
    print("3 by 3 grid of points, paths into each:", [[P[i, j] for j in range(3)] for i in range(3)])


if __name__ == "__main__":
    week5()
    week6()
    week7()
