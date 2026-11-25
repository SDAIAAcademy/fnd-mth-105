# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
# %% [markdown]
# # Lab 5.1 · Hash collisions and the birthday problem, by formula and by brute force
#
# Week 5 · Session 1 (Counting arrangements and collisions) · 105 min.
#
# The volunteer centre wants a short check-in code for each volunteer, cut from a hash of the
# volunteer code, so that people can type it at an event. Short codes collide. You count codes,
# arrangements and selections with the sum and product rules, compute the chance of a collision
# exactly, check every formula against a brute-force count on small cases, and choose a code length
# the centre can live with.
#
# **AI policy.** AI-tutor: it may point at a gap, never write the answer (`labs/tutor/TUTOR.md`).
#
# **Tasks**
# - [ ] 1 · Set up; sum and product rules (10 min)
# - [ ] 2 · Arrangements and selections, two ways (15 min)
# - [ ] 3 · Short check-in codes from a hash (10 min)
# - [ ] 4 · Collision-free count: formula and brute force (20 min)
# - [ ] 5 · The birthday problem exactly, with fractions (15 min)
# - [ ] 6 · Expected colliding pairs against those issued (15 min)
# - [ ] 7 · Pigeonhole: when a collision is certain (10 min)
# - [ ] 8 · Choose the code length and record it (10 min)
# - [ ] ✱ Stretch · Count the shared birthdays in the register and compare with the formula

# %%
import os, sys, subprocess
from pathlib import Path

IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    REPO_URL = "https://github.com/SDAIAAcademy/fnd-mth-105.git"
    if not Path("/content/fnd-mth-105").exists():
        subprocess.run(["git", "clone", "-q", REPO_URL, "/content/fnd-mth-105"], check=True)
    os.chdir("/content/fnd-mth-105/labs")
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements-colab.txt"], check=True)
else:
    while not Path("_tools").exists() and Path.cwd() != Path.cwd().parent:
        os.chdir("..")  # solutions/ notebooks run from labs/
sys.path.insert(0, os.getcwd())

import hashlib
import itertools
import math
from collections import Counter
from fractions import Fraction
import dm as U

HEX = "0123456789ABCDEF"
VOLS = [r["vol_code"] for r in U.load_csv("register.csv")]
print(len(VOLS), "volunteers, from", VOLS[0], "to", VOLS[-1])

# %% [markdown]
# ## 1 · Sum and product rules
#
# A code is a string over the 16 symbols 0 to 9 and A to F.
#
# **By hand first:** how many codes of exactly 2 symbols are there (product rule)? How many codes of
# 1, 2 or 3 symbols in all (sum rule over the three lengths)? Write them in `hand`. Then count by
# listing every code with `itertools.product`.

# %%
hand = {"length 2": None, "lengths 1 to 3": None}   # ✏️ your two counts

def count_codes(lengths):
    # BEGIN SOLUTION
    return sum(1 for L in lengths for _ in itertools.product(HEX, repeat=L))
    # END SOLUTION

# %%
try:
    listed = {"length 2": count_codes([2]), "lengths 1 to 3": count_codes([1, 2, 3])}
except NotImplementedError:
    listed = {"length 2": 256, "lengths 1 to 3": 4368}
print("by listing:", listed, "| by the rules:", {"length 2": 16 ** 2, "lengths 1 to 3": 16 + 16 ** 2 + 16 ** 3})
U.check(listed == {"length 2": 16 ** 2, "lengths 1 to 3": 16 + 16 ** 2 + 16 ** 3}, "listing agrees with the product and sum rules")
if None not in hand.values():
    U.check(hand == listed, "hand and code agree")

# %% [markdown]
# ## 2 · Permutations and combinations
#
# From 10 volunteers the coordinator picks a panel of 3 (a **selection**: order does not matter)
# or a lead, a deputy and a note-taker (an **arrangement**: order matters). Write
# `perm_formula(n, k)` = n! / (n − k)! and `comb_formula(n, k)` = n! / (k! (n − k)!) with
# `math.factorial`, then compare with the number of tuples listed by `itertools.permutations` and
# `itertools.combinations` for every k from 0 to n, for n up to 9.

# %%
def perm_formula(n, k):
    # BEGIN SOLUTION
    return math.factorial(n) // math.factorial(n - k)
    # END SOLUTION

def comb_formula(n, k):
    # BEGIN SOLUTION
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    # END SOLUTION

# %%
try:
    mism = [(n, k) for n in range(0, U.pick(10, 7)) for k in range(0, n + 1)
            if perm_formula(n, k) != sum(1 for _ in itertools.permutations(range(n), k))
            or comb_formula(n, k) != sum(1 for _ in itertools.combinations(range(n), k))]
    print("panels of 3 from 10:", comb_formula(10, 3), "| ordered roles:", perm_formula(10, 3))
except NotImplementedError:
    mism = []
U.check(mism == [], "formula and enumeration agree for every n and k tried")

# %% [markdown]
# **Look at** the ratio of the two answers: 720 / 120 = 6 = 3!, the number of ways to order each
# panel. That is the proof of the combination formula in one line.

# %% [markdown]
# ## 3 · Short check-in codes
#
# The centre's idea: hash the volunteer code with SHA-256 and keep the first k hexadecimal
# symbols. Write `checkin(vol, k)`. Then, for k = 3, 4, 5 and 6, count how many different codes the
# 4,000 volunteers get and how many volunteers share their code with someone.

# %%
def checkin(vol, k):
    # BEGIN SOLUTION
    return hashlib.sha256(vol.encode("utf-8")).hexdigest()[:k].upper()
    # END SOLUTION

# %%
def code_table(k):
    try:
        codes = [checkin(v, k) for v in VOLS]
    except NotImplementedError:
        codes = [hashlib.sha256(v.encode("utf-8")).hexdigest()[:k].upper() for v in VOLS]
    c = Counter(codes)
    return c

rows = []
for k in (3, 4, 5, 6):
    c = code_table(k)
    shared = sum(m for m in c.values() if m > 1)
    pairs = sum(math.comb(m, 2) for m in c.values())
    rows.append([k, f"{16 ** k:,}", len(c), shared, pairs])
U.table(rows, ["k", "possible codes", "distinct codes", "volunteers sharing", "colliding pairs"])
U.keep("w5_code_rows", rows)
print("example with k = 4:", VOLS[0], "->", hashlib.sha256(VOLS[0].encode("utf-8")).hexdigest()[:4].upper())

# %% [markdown]
# ## 4 · The collision-free count
#
# n volunteers each get one of N codes: N to the power n assignments in all (product rule). In how
# many are all n codes different? First code: N choices, second: N − 1, and so on, so
# N · (N − 1) · … · (N − n + 1). Write `distinct_formula(N, n)` and `distinct_brute(N, n)`, which
# lists every assignment and counts those without a repeat. Compare them on every N up to 7 and
# every n up to N + 1.

# %%
def distinct_formula(N, n):
    # BEGIN SOLUTION
    return math.perm(N, n) if n <= N else 0
    # END SOLUTION

def distinct_brute(N, n):
    # BEGIN SOLUTION
    return sum(1 for a in itertools.product(range(N), repeat=n) if len(set(a)) == n)
    # END SOLUTION

# %%
top = U.pick(7, 5)
try:
    table = [(N, n, distinct_formula(N, n), distinct_brute(N, n)) for N in range(1, top + 1) for n in range(1, N + 2)]
except NotImplementedError:
    table = [tuple(r) for r in U.reference("w5_distinct")]
table = U.keep("w5_distinct", table)
U.table([r for r in table if r[0] == top], ["N", "n", "formula", "brute force"])
U.check(all(r[2] == r[3] for r in table), "formula and brute force agree on every case")

# %% [markdown]
# **Look at** the last row: with n = N + 1 there is no collision-free assignment at all. Task 7
# names that.

# %% [markdown]
# ## 5 · The birthday problem, exactly
#
# The chance that n codes drawn from N are all different is the collision-free count divided by
# all assignments: N(N − 1)…(N − n + 1) / Nⁿ. Compute it **exactly** with `Fraction`, then find the
# smallest n for which a shared value is more likely than not, for N = 365 (birthdays) and for
# N = 16⁴ (four-symbol codes).

# %%
def p_all_distinct(N, n):
    # BEGIN SOLUTION
    p = Fraction(1)
    for i in range(n):
        p *= Fraction(N - i, N)
    return p
    # END SOLUTION

def smallest_n_over_half(N):
    n = 1
    while 1 - p_all_distinct(N, n) <= Fraction(1, 2):
        n += 1
    return n

# %%
try:
    n365, n4 = smallest_n_over_half(365), smallest_n_over_half(16 ** 4)
    p23 = float(1 - p_all_distinct(365, 23))
    exact_small = p_all_distinct(4, 3) == Fraction(distinct_brute(4, 3), 4 ** 3)
except NotImplementedError:
    n365, n4, p23, exact_small = 23, 302, 0.5073, True
print("N = 365: smallest n with a shared value more likely than not:", n365, f"| chance at 23: {p23:.4f}")
print("N = 16^4 = 65,536:", n4, "codes")
U.check(n365 == 23 and exact_small, "23 for birthdays; the fraction agrees with brute force at N = 4, n = 3")

# %% [markdown]
# **Look at** n4 against √N = 256: the threshold grows like the square root of N, about 1.18 √N.
# That is why short codes collide so much earlier than people expect.

# %% [markdown]
# ## 6 · Expected colliding pairs
#
# Count the pairs: over all Nⁿ assignments, how many (assignment, pair of volunteers with the same
# code) are there? Each of the C(n, 2) pairs shares a code in N · N^(n−2) assignments, so the
# average number of colliding pairs per assignment is C(n, 2) / N. Check that average by brute force
# on small N and n, then compare C(4000, 2) / 16^k with the pairs counted in task 3.

# %%
def avg_pairs_brute(N, n):
    # BEGIN SOLUTION
    total = sum(sum(1 for i, j in itertools.combinations(range(n), 2) if a[i] == a[j])
                for a in itertools.product(range(N), repeat=n))
    return Fraction(total, N ** n)
    # END SOLUTION

# %%
try:
    small_ok = all(avg_pairs_brute(N, n) == Fraction(math.comb(n, 2), N) for N in range(1, 6) for n in range(1, 6))
except NotImplementedError:
    small_ok = True
U.check(small_ok, "the average number of colliding pairs is C(n, 2) / N on every small case")
cmp = [[r[0], round(math.comb(4000, 2) / 16 ** r[0], 1), r[4]] for r in rows]
U.table(cmp, ["k", "expected pairs C(n,2)/N", "pairs counted"])
U.keep("w5_expected_vs_counted", cmp)

# %% [markdown]
# **Look at** the two columns. The counted number is one draw; the formula is the average over all
# possible draws, so they are close but not equal.

# %% [markdown]
# ## 7 · Pigeonhole
#
# If n items go into N boxes and n > N, some box holds at least two; more precisely, some box holds
# at least ⌈n / N⌉. For k = 2 (256 codes), what is the guarantee for 4,000 volunteers, and what is
# the largest group that actually shares a code? For k = 3 (4,096 codes) is any collision
# guaranteed?

# %%
def pigeonhole_guarantee(n, N):
    # BEGIN SOLUTION
    return -(-n // N)
    # END SOLUTION

# %%
try:
    g2, g3 = pigeonhole_guarantee(4000, 16 ** 2), pigeonhole_guarantee(4000, 16 ** 3)
except NotImplementedError:
    g2, g3 = 16, 1
largest2 = max(code_table(2).values())
print("k = 2: guaranteed at least", g2, "on one code; largest group found:", largest2)
print("k = 3: guaranteed at least", g3, "(no collision is guaranteed), yet pairs found:", rows[0][4])
U.check(g2 == 16 and largest2 >= g2 and g3 == 1, "the guarantee holds and is a lower bound")

# %% [markdown]
# ## 8 · Choose the code length
#
# The operations lead accepts a chance of at most 1 in 100 that two of the 4,000 volunteers share
# a code. Find the smallest k, using your exact formula (floats are accurate enough here). Then
# repeat for a centre of 40,000 volunteers.

# %%
def smallest_k(n, risk):
    # BEGIN SOLUTION
    k = 1
    while True:
        N, p = 16 ** k, 1.0
        for i in range(n):
            p *= (N - i) / N
        if 1 - p <= risk:
            return k, 1 - p
        k += 1
    # END SOLUTION

# %%
try:
    k4000, r4000 = smallest_k(4000, 0.01)
    k40000, r40000 = smallest_k(U.pick(40000, 4000), 0.01)
except NotImplementedError:
    (k4000, r4000), (k40000, r40000) = U.reference("w5_choice")
U.keep("w5_choice", [[k4000, r4000], [k40000, r40000]])
print(f"4,000 volunteers: k = {k4000}, chance of a shared code {r4000:.4f}")
print(f"40,000 volunteers: k = {k40000}, chance of a shared code {r40000:.4f}")
U.check(k4000 == 8, "eight symbols for 4,000 volunteers")

# %% [markdown]
# *Your note for the operations lead (code length, the chance it leaves, and what to do when two
# volunteers still share a code at check-in):*

# %% [markdown]
# BEGIN SOLUTION
# Eight symbols give a chance of about 0.19% that any two of 4,000 volunteers share a code; seven
# would give about 3%. Growth to 40,000 needs ten symbols for the same risk. Since a collision
# stays possible, check-in must look up the code and, when two volunteers match, ask for a second
# factor (the badge), rather than trusting the code alone.
# END SOLUTION

# %% [markdown]
# ## ✱ Stretch
#
# Count the pairs of volunteers in the register who share a birthday (month and day) and compare
# with C(4000, 2) / 365. Then explain the difference: are birthdays uniform over the year, and
# what does 29 February do?

# %% [markdown]
# ## Check yourself
#
# <details><summary>1. Why does the chance of a shared code pass one half near 1.18 √N and not near N / 2?</summary>
# Because what matters is pairs, and n codes form C(n, 2), about n²/2, pairs. Each pair collides
# with chance 1/N, so collisions become likely once n² is comparable to N.</details>
#
# <details><summary>2. When does the pigeonhole principle guarantee a collision, and what does it not tell you?</summary>
# When there are more items than codes. It says nothing about how likely a collision is below that
# point: with 4,000 volunteers and 4,096 codes there is no guarantee, yet collisions are almost
# certain.</details>
#
# <details><summary>3. Why check a formula against brute force on small cases?</summary>
# Brute force counts by definition, so it catches an off-by-one, a wrong bracket or a misread
# rule in the formula. It only works on small cases; the formula is what scales.</details>
#
# ## Carry forward
#
# Nothing to save. Week 6 counts people instead of codes: how many share each combination of birth
# date, sex and district.
