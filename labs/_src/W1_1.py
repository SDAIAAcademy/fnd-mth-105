# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
# %% [markdown]
# # Lab 1.1 · Sets, functions and joins in code
#
# Week 1 · Session 1 (Sets, functions and relations) · 90 min.
#
# *An added lab, beyond the catalog entry's five lab lines.*
#
# You are the new data analyst of the community volunteer centre. Its tables are sets of tuples:
# volunteers, check-in badges, events, shifts and who works which shift. You check whether the
# badge map is really a function and what kind, compose "volunteer works shift" with "shift belongs
# to event", and compare that composition with what an SQL join returns.
#
# **AI policy.** AI-tutor: it may point at a gap, never write the answer (`labs/tutor/TUTOR.md`).
#
# **Tasks**
# - [ ] 1 · Set up and load the centre's tables (10 min)
# - [ ] 2 · Set operations and Cartesian products, by hand and in code (10 min)
# - [ ] 3 · Is the badge map a function? Total, injective, surjective (20 min)
# - [ ] 4 · Shift to event: a function onto the events? (10 min)
# - [ ] 5 · Inverse and composition of relations (15 min)
# - [ ] 6 · Compose assignments with shifts, then join them in SQL (20 min)
# - [ ] 7 · Record what the coordinator should fix (5 min)
# - [ ] ✱ Stretch · Show on the three tables that composing relations is associative

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

import itertools
import sqlite3
import dm as U

# %% [markdown]
# ## 1 · Load the tables
#
# Each table is read as a set. `badges` is a set of pairs (volunteer, badge number): a relation.
# Only the first 300 volunteers of the register take part in events this month.

# %%
register = U.load_csv("register.csv")
V = {r["vol_code"] for r in register[:300]}                 # the 300 active volunteers
badges = U.pairs("badges.csv", "vol_code", "badge")          # relation: volunteer -> badge
shift_event = U.pairs("shifts.csv", "shift", "event")        # relation: shift -> event
works = U.pairs("assignments.csv", "vol_code", "shift")      # relation: volunteer -> shift
EVENTS = {r["event"] for r in U.load_csv("events.csv")}
SHIFTS = {s for s, _ in shift_event}
print(len(V), "volunteers |", len(badges), "badge pairs |", len(SHIFTS), "shifts |", len(EVENTS), "events |", len(works), "assignments")

# %% [markdown]
# ## 2 · Set operations and Cartesian products
#
# **By hand first.** A = {PD-01, PD-02} and B = {early, middle, late}. How many pairs does A × B
# hold? Write it in `hand_AxB`. Then write `product_size(A, B)` that builds the product with
# `itertools.product` and returns its size, and use set operations for the questions below.

# %%
hand_AxB = None   # ✏️ your hand answer

def product_size(A, B):
    # BEGIN SOLUTION
    return len(set(itertools.product(A, B)))
    # END SOLUTION

# %%
A, B = {"PD-01", "PD-02"}, {"early", "middle", "late"}
DISTRICTS = {r["district"] for r in register}
PARTS = {"early", "middle", "late"}
try:
    n_small, n_slots = product_size(A, B), product_size(DISTRICTS, PARTS)
except NotImplementedError:
    n_small, n_slots = 6, 36
print("|A x B| =", n_small, "| district x part slots =", n_slots)
U.check(n_slots == len(DISTRICTS) * len(PARTS), "the size of a product is the product of the sizes")
if hand_AxB is not None:
    U.check(hand_AxB == n_small, "hand and code agree")

with_badge = {v for v, _ in badges}
assigned = {v for v, _ in works}
print("assigned but no badge:", sorted(assigned - with_badge))
print("badge but never assigned:", len(with_badge - assigned), "| both:", len(with_badge & assigned))

# %% [markdown]
# **Look at** the first line: those volunteers will reach a shift and fail check-in.

# %% [markdown]
# ## 3 · Is the badge map a function?
#
# A relation R from X to Y is a **function** when every x in X has exactly one y with (x, y) in R.
# It is **injective** when no two x share a y, **surjective** onto Y when every y is reached, and
# **bijective** when it is both. Write the four tests. `badge_numbers` is the set of numbers the
# centre printed: BD-0001 to BD-0999.

# %%
def images(R, x):
    return {y for a, y in R if a == x}

def is_function(R, X):
    # BEGIN SOLUTION
    return all(len(images(R, x)) == 1 for x in X)
    # END SOLUTION

def is_injective(R):
    # BEGIN SOLUTION
    ys = [y for _, y in R]
    return len(ys) == len(set(ys))
    # END SOLUTION

def is_surjective(R, Y):
    # BEGIN SOLUTION
    return {y for _, y in R} >= set(Y)
    # END SOLUTION

# %%
badge_numbers = {f"BD-{i:04d}" for i in range(1, 1000)}
try:
    verdict = {"function on V": is_function(badges, V), "injective": is_injective(badges),
               "surjective": is_surjective(badges, badge_numbers)}
except NotImplementedError:
    verdict = U.reference("w1_badge_verdict")
verdict = U.keep("w1_badge_verdict", verdict)
print(verdict)
missing = sorted(x for x in V if not images(badges, x))
shared = sorted(y for y in {y for _, y in badges} if sum(1 for _, b in badges if b == y) > 1)
print("volunteers with no badge:", missing)
print("badge numbers issued twice:", shared)
U.check(verdict == {"function on V": False, "injective": False, "surjective": False}, "the badge map fails all three tests")
U.check(len(missing) == 2 and len(shared) == 3, "two volunteers lack a badge and three numbers are shared")

# %% [markdown]
# **Look at** why each test fails. "Not a function on V" comes from the two volunteers with no
# badge, not from anyone holding two. Not surjective is harmless here (unused numbers); not
# injective is not: two people would check in as one.

# %% [markdown]
# ## 4 · Shift to event
#
# Every shift belongs to exactly one event. Run your tests on `shift_event` with X = the shifts and
# Y = the events, and count the shifts per event.

# %%
try:
    se = {"function": is_function(shift_event, SHIFTS), "injective": is_injective(shift_event),
          "surjective": is_surjective(shift_event, EVENTS)}
except NotImplementedError:
    se = {"function": True, "injective": False, "surjective": True}
per_event = {e: len([s for s, f in shift_event if f == e]) for e in EVENTS}
print(se, "| shifts per event:", sorted(set(per_event.values())))
U.check(se == {"function": True, "injective": False, "surjective": True}, "a function onto the events, three shifts each")

# %% [markdown]
# ## 5 · Inverse and composition
#
# The **inverse** of R swaps each pair. The **composition** of R (X to Y) followed by S (Y to Z) is
# the set of (x, z) such that some y has (x, y) in R and (y, z) in S. Write both.

# %%
def inverse(R):
    # BEGIN SOLUTION
    return {(y, x) for x, y in R}
    # END SOLUTION

def compose(R, S):
    """R followed by S."""
    # BEGIN SOLUTION
    by_first = {}
    for y, z in S:
        by_first.setdefault(y, set()).add(z)
    return {(x, z) for x, y in R for z in by_first.get(y, ())}
    # END SOLUTION

# %%
R_small = {(1, "a"), (2, "a"), (3, "b")}
S_small = {("a", "X"), ("b", "Y"), ("b", "Z")}
try:
    small = compose(R_small, S_small)
    inv_ok = inverse(inverse(badges)) == badges
except NotImplementedError:
    small, inv_ok = {(1, "X"), (2, "X"), (3, "Y"), (3, "Z")}, True
print("R then S:", sorted(small))
U.check(small == {(1, "X"), (2, "X"), (3, "Y"), (3, "Z")}, "composition on the small case")
U.check(inv_ok, "the inverse of the inverse is the relation itself")
try:
    print("is the inverse of the badge map a function on its badges?", is_function(inverse(badges), {y for _, y in badges}))
except NotImplementedError:
    pass

# %% [markdown]
# ## 6 · Composition against an SQL join
#
# `works` composed with `shift_event` relates each volunteer to the events they work at. Compute it
# with `compose`. Then load both tables into an in-memory SQLite database and run the join. A join
# returns one row per matching pair of rows, so it can repeat a (volunteer, event) pair; a
# composition is a set. Write `join_rows()` returning the list of rows of the join.

# %%
db = sqlite3.connect(":memory:")
db.execute("create table works (vol_code text, shift text)")
db.execute("create table shifts (shift text, event text)")
db.executemany("insert into works values (?, ?)", sorted(works))
db.executemany("insert into shifts values (?, ?)", sorted(shift_event))

def join_rows():
    # BEGIN SOLUTION
    q = "select w.vol_code, s.event from works w join shifts s on w.shift = s.shift"
    return db.execute(q).fetchall()
    # END SOLUTION

# %%
try:
    vol_event = compose(works, shift_event)
except NotImplementedError:
    vol_event = {tuple(p) for p in U.reference("w1_vol_event")}
vol_event = U.keep("w1_vol_event", vol_event)
try:
    rows = join_rows()
except NotImplementedError:
    rows = db.execute("select w.vol_code, s.event from works w join shifts s on w.shift = s.shift").fetchall()
repeats = len(rows) - len(set(rows))
print("join rows:", len(rows), "| distinct pairs:", len(set(rows)), "| composition pairs:", len(vol_event), "| repeated rows:", repeats)
U.check(set(rows) == vol_event, "the distinct rows of the join are the composition")
U.check(repeats > 0, "the join repeats pairs: someone works two shifts of one event")
twice = sorted({r for r in rows if rows.count(r) > 1})[:5]
print("first pairs that repeat:", twice)
db.close()

# %% [markdown]
# **Look at** the gap between the two counts. A report that counts join rows as "volunteers at
# events" overcounts by that many. `select distinct` gives the composition.

# %% [markdown]
# ## 7 · Record
#
# Write two or three sentences for the volunteer coordinator: which badges to reissue, who needs a
# badge before their shift, and how to count volunteers per event without overcounting. (No code.)

# %% [markdown]
# *Your note:*

# %% [markdown]
# ## ✱ Stretch
#
# Build `event_district` from `events.csv` (event to district). Check in code that
# `compose(compose(works, shift_event), event_district)` equals
# `compose(works, compose(shift_event, event_district))`. Then explain why it must, for any three
# relations, from the definition of composition.

# %% [markdown]
# ## Check yourself
#
# <details><summary>1. A map gives every volunteer one badge, and no badge twice. Which property is still missing for a bijection onto the printed numbers?</summary>
# Surjectivity: every printed number would have to be used. A bijection needs function, injective
# and surjective together.</details>
#
# <details><summary>2. Why can a join return more rows than the composition has pairs?</summary>
# A join is a multiset: one row for each pair of matching rows. Two shifts of the same event give
# the same (volunteer, event) pair twice; the composition, a set, keeps it once.</details>
#
# <details><summary>3. |X| = 12 and |Y| = 3. How many pairs does X × Y have, and how many relations from X to Y exist?</summary>
# 36 pairs. A relation is any subset of them, so there are 2 to the power 36 relations.</details>
#
# ## Carry forward
#
# Nothing to save. Week 3 classifies relations with the same kind of tests; it starts from the
# files in `data/`.
