# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
# %% [markdown]
# # Lab 6.1 · Re-identification risk counted from birth date, sex and postal district in a synthetic register
#
# Week 6 · Session 1 (Inclusion-exclusion and linkage risk) · 105 min.
#
# A partner asks the volunteer centre for its register "without identifiers". The register holds
# no names: its direct identifier is the volunteer code, and the plan is to drop that column and
# send the rest. Before anything leaves the centre, the data protection officer asks you to count:
# how many people would still stand alone on birth date, sex and postal district? You count class
# sizes, compare with what the product rule predicts, generalise until no one stands alone, check
# inclusion-exclusion with sets, and link a sign-in sheet the centre once published back to the
# register.
#
# Everything here is synthetic: the register was generated with a fixed seed and its people are
# codes, not persons.
#
# **AI policy.** AI-tutor: it may point at a gap, never write the answer (`labs/tutor/TUTOR.md`).
# Nothing from the register goes into any AI tool: paste only code and error messages.
#
# **Tasks**
# - [ ] 1 · Set up; the extract without the volunteer code (10 min)
# - [ ] 2 · People per combination of the three columns (15 min)
# - [ ] 3 · Product rule: combinations and expected uniques (15 min)
# - [ ] 4 · Generalise: birth year, five-year bands, district groups (20 min)
# - [ ] 5 · Inclusion-exclusion, checked with sets (15 min)
# - [ ] 6 · Link the posted sign-in sheet (15 min)
# - [ ] 7 · Record for the data protection officer (15 min)
# - [ ] ✱ Stretch · Find the most detailed release in which every combination holds five people

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

import datetime as dt
from collections import Counter
import dm as U

# %% [markdown]
# ## 1 · The extract
#
# Drop the volunteer code and keep birth date, sex, postal district and skills: the extract the
# partner would receive.

# %%
register = U.load_csv("register.csv")
extract = [{k: r[k] for k in ("birth_date", "sex", "district", "skills")} for r in register]
print(len(extract), "rows; columns:", list(extract[0]))
print("first row:", extract[0])

# %% [markdown]
# ## 2 · Class sizes
#
# Group the rows by the **quasi-identifiers** (birth date, sex, district): columns that are not
# identifiers alone but can single a person out together. A group of size 1 is a person who is
# unique in the extract. Write `class_sizes(rows, key)` returning a `Counter` from each
# combination to the number of rows that have it; `key` is a function from a row to its
# combination.

# %%
def class_sizes(rows, key):
    # BEGIN SOLUTION
    return Counter(key(r) for r in rows)
    # END SOLUTION

def full(r):
    return (r["birth_date"], r["sex"], r["district"])

def summary(sizes, n):
    """People in classes of size 1, 2, 3 to 4, 5 or more; share unique; smallest class."""
    people = Counter()
    for s in sizes.values():
        people["1" if s == 1 else "2" if s == 2 else "3-4" if s <= 4 else "5+"] += s
    return {"combinations used": len(sizes), "unique people": people["1"], "share unique": round(people["1"] / n, 4),
            "in classes of 2": people["2"], "in classes of 3-4": people["3-4"], "in classes of 5+": people["5+"],
            "smallest class": min(sizes.values())}

# %%
try:
    sizes = class_sizes(extract, full)
except NotImplementedError:
    sizes = Counter(full(r) for r in extract)
s_full = U.keep("w6_full", summary(sizes, len(extract)))
for k, v in s_full.items():
    print(f"{k:20s} {v}")
U.check(s_full["share unique"] > 0.9, "more than nine in ten people are unique on the three columns")

# %% [markdown]
# **Look at** the first two lines. Without the code column, more than nine people in ten can still
# be singled out by anyone who knows their birth date, sex and district: a neighbour, a colleague,
# a relative.

# %% [markdown]
# ## 3 · What the product rule predicts
#
# The number of possible combinations is (days in the birth-date range) × 2 × 12. If n people were
# spread evenly at random over M combinations, the expected number of people alone in theirs would
# be n (1 − 1/M)ⁿ⁻¹: each person is unique when the n − 1 others all land elsewhere. Write
# `possible(rows)` (the product) and `expected_unique(n, M)`, and compare with your count.

# %%
dates = sorted(dt.date.fromisoformat(r["birth_date"]) for r in extract)

def possible(rows):
    # BEGIN SOLUTION
    days = (dates[-1] - dates[0]).days + 1
    return days * len({r["sex"] for r in rows}) * len({r["district"] for r in rows})
    # END SOLUTION

def expected_unique(n, M):
    # BEGIN SOLUTION
    return n * (1 - 1 / M) ** (n - 1)
    # END SOLUTION

# %%
try:
    M = possible(extract)
    eu = expected_unique(len(extract), M)
except NotImplementedError:
    M, eu = U.reference("w6_product")
U.keep("w6_product", [M, eu])
print(f"possible combinations: {M:,} | people per combination: {len(extract) / M:.4f}")
print(f"expected unique if spread evenly: {eu:,.0f} | counted: {s_full['unique people']:,}")
years = len({r["birth_date"][:4] for r in extract})
try:
    eu_year = expected_unique(len(extract), years * 2 * 12)
except NotImplementedError:
    eu_year = U.reference("w6_product_year")
U.keep("w6_product_year", eu_year)
print(f"by birth year instead: {years * 2 * 12:,} combinations; expected unique if spread evenly: {eu_year:,.0f}")

# %% [markdown]
# **Look at** the first comparison: with far more combinations than people, the even-spread
# formula predicts almost exactly how many people stand alone. Keep the second number for task 4:
# with birth years, people are not spread evenly (few volunteers were born in the earliest years),
# and the count will differ from the formula.

# %% [markdown]
# ## 4 · Generalise
#
# The guideline the data protection officer follows lists generalisation (ages into bands) and
# aggregation (birth year instead of full date) among its example techniques. Try five releases
# and print, for each, the number of possible combinations, the share of unique people and the
# smallest class. The district groups merge the twelve districts into four:
# PD-01 to PD-03, PD-04 to PD-06, PD-07 to PD-09, PD-10 to PD-12.

# %%
def zone(d):
    return "Z" + str((int(d[3:]) - 1) // 3 + 1)

def band(year, width):
    lo = year - (year - 1955) % width
    return f"{lo}-{lo + width - 1}"

RELEASES = {
    "date, sex, district": lambda r: (r["birth_date"], r["sex"], r["district"]),
    "year, sex, district": lambda r: (r["birth_date"][:4], r["sex"], r["district"]),
    "5-year band, sex, district": lambda r: (band(int(r["birth_date"][:4]), 5), r["sex"], r["district"]),
    "5-year band, sex, district group": lambda r: (band(int(r["birth_date"][:4]), 5), r["sex"], zone(r["district"])),
    "10-year band, sex, district group": lambda r: (band(int(r["birth_date"][:4]), 10), r["sex"], zone(r["district"])),
}

# %%
rows = []
results = {}
for name, key in RELEASES.items():
    try:
        sz = class_sizes(extract, key)
    except NotImplementedError:
        sz = Counter(key(r) for r in extract)
    sm = summary(sz, len(extract))
    results[name] = sm
    rows.append([name, sm["combinations used"], sm["unique people"], f"{sm['share unique']:.1%}", sm["smallest class"]])
results = U.keep("w6_releases", results)
U.table(rows, ["release", "combinations used", "unique people", "share unique", "smallest class"])
U.check(results["10-year band, sex, district group"]["unique people"] == 0, "the coarsest release leaves no one alone")

# %% [markdown]
# **Look at** the year row against task 3's second number: more people are unique by birth year
# than the even spread predicts, because the earliest years hold few volunteers. And look at the
# price of each step: every row of the table loses detail an analyst might need (age within the
# band, the exact district).

# %% [markdown]
# ## 5 · Inclusion-exclusion
#
# The partner could also receive two separate tables: one by (year, sex), one by (year, district).
# Let A be the people unique in the first, B those unique in the second. How many people are unique
# in at least one table? Compute |A ∪ B| as |A| + |B| − |A ∩ B| from the three counts, and check it
# against the size of the union of the two sets. Then do the same for three tables, adding C, the
# people unique by (sex, district, skills).

# %%
def unique_people(key):
    sz = Counter(key(r) for r in register)
    return {r["vol_code"] for r in register if sz[key(r)] == 1}

A = unique_people(lambda r: (r["birth_date"][:4], r["sex"]))
B = unique_people(lambda r: (r["birth_date"][:4], r["district"]))
C = unique_people(lambda r: (r["sex"], r["district"], r["skills"]))

def union_two(a, b, ab):
    # BEGIN SOLUTION
    return a + b - ab
    # END SOLUTION

def union_three(a, b, c, ab, ac, bc, abc):
    # BEGIN SOLUTION
    return a + b + c - ab - ac - bc + abc
    # END SOLUTION

# %%
print("|A| =", len(A), "|B| =", len(B), "|C| =", len(C), "|A and B| =", len(A & B))
try:
    two = union_two(len(A), len(B), len(A & B))
    three = union_three(len(A), len(B), len(C), len(A & B), len(A & C), len(B & C), len(A & B & C))
except NotImplementedError:
    two, three = len(A | B), len(A | B | C)
print("by inclusion-exclusion:", two, three, "| by the union of the sets:", len(A | B), len(A | B | C))
U.check(two == len(A | B) and three == len(A | B | C), "inclusion-exclusion agrees with the sets")
U.keep("w6_ie", [len(A), len(B), len(C), len(A & B), two, three])

# %% [markdown]
# **Look at** what the union means: separate tables that are each "safe enough" combine. A person
# unique in either table can be found.

# %% [markdown]
# ## 6 · Linking a published sheet
#
# Last year the centre posted a sign-in sheet of one event with birth date, sex, district and the
# shift part each person worked, and no codes (`data/signin_sheet.csv`). Link it to the register:
# for each row, count the register rows with the same birth date, sex and district. A row that
# matches exactly one register row is **re-identified**: its volunteer code, skills and consent
# flags are now attached to the shift that person worked. Write `matches(row)`.

# %%
sheet = U.load_csv("signin_sheet.csv")
by_triple = {}
for r in register:
    by_triple.setdefault(full(r), []).append(r["vol_code"])

def matches(row):
    # BEGIN SOLUTION
    return by_triple.get(full(row), [])
    # END SOLUTION

# %%
try:
    m = [len(matches(r)) for r in sheet]
except NotImplementedError:
    m = U.reference("w6_link")
m = U.keep("w6_link", m)
print("sheet rows:", len(sheet), "| matched to exactly one volunteer:", m.count(1),
      "| to two or more:", sum(1 for x in m if x > 1), "| to none:", m.count(0))
U.check(m.count(1) + sum(1 for x in m if x > 1) == len(sheet), "every sheet row matches the register")

# %% [markdown]
# ## 7 · Record
#
# Write a note of five to eight sentences for the data protection officer. Use your counts. Say:
# why dropping the volunteer code does not make the extract anonymous; what the Law's definition
# of personal data says about indirect identification (quoted in the cell below); which release of
# task 4 you would send, with its smallest class; and what the published sign-in sheet shows.
#
# > Personal Data Protection Law, Article 1 (SDAIA's English text): personal data includes any data
# > that "may directly or indirectly make it possible to identify an individual".
#
# The centre's own rule, not a legal threshold: a table leaves the centre only if every
# combination holds at least five people.

# %% [markdown]
# BEGIN SOLUTION
# Dropping the volunteer code removes the direct identifier only. On birth date, sex and district
# 3,956 of the 4,000 volunteers (98.9%) are still unique, so anyone who knows those three facts
# about a person can find their row: the extract makes identification indirectly possible and
# remains personal data under the Law's definition. Birth year instead of the full date still
# leaves 245 people unique, five-year bands 19, and five-year bands with the four district groups
# 6. Ten-year bands with the district groups leave no one unique and a smallest group of 8, which
# meets the centre's rule of five, at the cost of exact age and district. Separate tables combine:
# 572 people are unique in at least one of three tables that each look harmless on their own. The
# sign-in sheet published last year matches every one of its 60 rows to exactly one volunteer,
# attaching codes, skills and consent flags to shifts: it should be taken down and the practice
# stopped. The analyst who prepares a release should not also approve it: the data protection
# officer signs off before anything leaves the centre.
# END SOLUTION

# %% [markdown]
# ## ✱ Stretch
#
# Search the releases you can build from (date, year, 5-year band, 10-year band) × (sex or not) ×
# (district, district group, no district) for the most detailed one whose smallest class is at
# least five. "Most detailed" is your choice to define: state it. What analysis does it rule out?

# %% [markdown]
# ## Check yourself
#
# <details><summary>1. The register has no names. Why is it still personal data?</summary>
# Because birth date, sex and district together single out most people, so the data makes it
# indirectly possible to identify them, which the Law's definition covers.</details>
#
# <details><summary>2. Why does the product rule predict more unique people than you counted?</summary>
# It assumes people spread evenly over the combinations. Real people cluster (ages, large
# districts), so some combinations are crowded and fewer people stand alone.</details>
#
# <details><summary>3. Two tables each leave few unique people. Why is releasing both riskier than either?</summary>
# A person unique in either table can be found: the risk is the union, |A| + |B| − |A ∩ B|, not the
# larger of the two.</details>
#
# ## Carry forward
#
# Nothing to save. Week 7 models the centre's nightly pipeline, which builds tables like these.
