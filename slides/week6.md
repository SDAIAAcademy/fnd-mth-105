---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
deck: "week6"
day: 6
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/slides/week6.html"
---

# Discrete Mathematics and Logic for Computing

## Week 6: Counting people: re-identification risk

Why removing the identifier column does not anonymise a register

#### [week6#title] Counting people: re-identification risk

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 6: Why removing the identifier column does not anonymise a register

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week6#agenda] Counting people: re-identification risk

*This week*

- **Session 1 · Inclusion-exclusion and linkage risk**: Inclusion-exclusion, the product rule over quasi-identifiers, class sizes in a register, generalisation, and personal versus anonymised data

#### [week6#review-week5] How many all-different assignments?

*Review · week 5*

**Question:** Five interns each draw one of 8 desk numbers. In how many of the 8⁵ draws do all five get different desks?

- A. 56
- B. 32,768
- C. 6,720
- D. 40,320

### Session 1: Inclusion-exclusion and linkage risk

#### [week6#s1] Inclusion-exclusion and linkage risk

*Session 1*

- Count the people who share each combination of quasi-identifiers and find who is unique
- Apply inclusion-exclusion to count records that meet at least one of several conditions, and check it with sets
- Explain why removing the direct identifier does not anonymise data, and what generalisation changes

#### [week6#ie-two] Add the sets, then subtract what you counted twice

*Block A · inclusion-exclusion*

**|A ∪ B| = |A| + |B| − |A ∩ B|**

|A| = 60, |B| = 50, |A ∩ B| = 20: |A ∪ B| = 90.

**Three sets:** |A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|

- **Why it works.** An element in exactly two of three sets is added twice and subtracted once; one in all three is added three times, subtracted three times, added once. Every element ends with count 1.

#### [week6#ie-code] A formula over counts can be checked against the sets themselves

*Checked with sets*

```python
# file: python
ie = len(A) + len(B) - len(A & B)
assert ie == len(A | B)
```

- The formula needs only counts: useful when the sets are held by different teams
- The union needs the elements themselves
- On data you hold, compute both: they must agree

#### [week6#check-ie] How many are in at least one?

*Checkpoint*

**Question:** Of a club's members, 45 read the newsletter, 30 attend events and 12 do both. How many do at least one of the two?

- A. 75
- B. 63
- C. 51
- D. 33

#### [week6#quasi-identifiers] Quasi-identifiers single people out in combination

*Block B · counting people*

- **Direct identifier.** Identifies a person alone: a name, a member number, a code assigned to one person. "Removing names" removes these columns.
- **Quasi-identifiers.** Shared by many people alone, but rare in combination: birth date, sex, postal district. Often known to neighbours and colleagues.

> **The question to count.** After the direct identifiers are gone, how many people are alone in their combination of quasi-identifiers?

#### [week6#product-people] When combinations outnumber people, almost everyone is unique

*The product rule again*

| A town of 20,000 adults, 10 districts | Combinations | People each |
| --- | --- | --- |
| Birth date (60 years), sex, district | 438,000 | 0.05 |
| Birth year, sex, district | 1,200 | 16.67 |
| 10-year band, sex, district | 120 | 166.67 |

If people spread evenly, n (1 − 1/M)ⁿ⁻¹ of them are alone among M combinations: 95.5% in the first row.

#### [week6#class-sizes] Count the people in each combination, then the people alone

*By hand first*

| Six members: year, sex, area | People |
| --- | --- |
| 1990, F, D1 | 2 |
| 1990, M, D1 | 1 |
| 1985, F, D2 | 2 |
| 1972, M, D3 | 1 |

- A combination held by one person is a **class of size 1**
- The smallest class says how alone the most exposed people are
- A release rule can set a smallest class, for example five

#### [week6#check-unique] What does the product rule predict?

*Checkpoint*

**Question:** A survey of 500 people keeps age in years (60 values), sex and one of 4 regions. Roughly how many combinations are there per person?

- A. 240,000
- B. 66
- C. about 0.48
- D. about 0.96

#### [week6#pdpl] Data that can identify a person indirectly is personal data

*Block C · the law*

- **Personal Data Protection Law, Article 1.** Personal data includes data that "may directly or indirectly make it possible to identify an individual" (SDAIA's English text).
- **SDAIA's anonymisation guideline.** Anonymised data "shall no longer be considered personal data"; the guideline asks that it be irreversible, with an assessment of re-identification. It states that it is not a binding legal document.

> **So.** An extract in which birth date, sex and district single people out still makes identification indirectly possible: removing the code column does not anonymise it.

#### [week6#generalise] Coarser columns make classes bigger and lose detail

*Generalisation*

**Birth date** 438,000 combinations in the parallel town → **Birth year** 1,200 → **10-year band** 120

- The guideline's examples include age bands and birth year in place of the full date
- Each step trades analysis detail for larger classes: say what the analysis loses

#### [week6#linkage] Releases combine: the risk is the union, not the safer of the two

*Linkage*

- Two tables, each with few people alone, are released: A and B are the people alone in each
- Anyone in A ∪ B can be found: |A| + |B| − |A ∩ B| people
- A list published elsewhere with the same columns links back row by row

- **Count before you publish.** For each row of a list to be posted, count how many people in your register share its quasi-identifiers. One means that row names a person.

#### [week6#check-anonymised] Is it anonymised?

*Checkpoint*

**Question:** A gym removes member numbers from its list and keeps full birth date, sex and home district. Most members are alone in their combination. Under the Law's definition, the list is:

- A. anonymised, since no identifier remains
- B. still personal data, since it makes identification indirectly possible
- C. pseudonymised, so outside the Law
- D. personal data only if more than half are unique

#### [week6#lab-6-1] Re-identification risk counted from birth date, sex and postal district in a synthetic register

Lab 6.1 · 105 min

Count who shares each combination of birth date, sex and district, generalise, and link a posted sheet back.

[W6_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W6_1.ipynb)

- [ ] Set up; the extract without the volunteer code (10 min)
- [ ] People per combination of the three columns (15 min)
- [ ] Product rule: combinations and expected uniques (15 min)
- [ ] Generalise: birth year, five-year bands, district groups (20 min)
- [ ] Inclusion-exclusion, checked with sets (15 min)
- [ ] Link the posted sign-in sheet (15 min)
- [ ] Record for the data protection officer (15 min)
- [ ] ✱ Stretch: Find the most detailed release in which every combination holds five people

#### [week6#debrief-reid] Without its codes, the register still singles out 98.9% of volunteers

*Debrief · lab 6.1*

| Release | Unique | Smallest class |
| --- | --- | --- |
| Date, sex, district | 3,956 | 1 |
| Year, sex, district | 245 | 1 |
| 5-year band, sex, district | 19 | 1 |
| 5-year band, sex, district group | 6 | 1 |
| 10-year band, sex, district group | 0 | 8 |

- Even spread predicts 3,966 unique; by year it predicts 193, against 245 counted
- Three tables, each modest alone: 572 people unique in at least one
- The posted sign-in sheet: all 60 rows match exactly one volunteer

#### [week6#wrap-up] Three things to keep

*Week 6 · wrap-up*

- **Subtract the overlap.** Inclusion-exclusion counts a union from its parts, and code can check it.
- **Count who is alone.** Removing the identifier column leaves quasi-identifiers; count the classes of size 1.
- **Releases add up.** Two safe-looking tables, or a posted list, can name people together.

#### [week6#next] Week 7: Graphs, topological order and growth

*Next*

Problem set 6 (60 minutes, AI off for the first attempt): labs/problem-sets/PS6.ipynb.
