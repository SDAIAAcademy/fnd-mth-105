---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
deck: "week5"
day: 5
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/slides/week5.html"
---

# Discrete Mathematics and Logic for Computing

## Week 5: Counting, collisions and the birthday problem

Sum and product rules, arrangements and selections, and when two codes must collide

#### [week5#title] Counting, collisions and the birthday problem

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 5: Sum and product rules, arrangements and selections, and when two codes must collide

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week5#agenda] Counting, collisions and the birthday problem

*This week*

- **Session 1 · Counting arrangements and collisions**: The sum and product rules, permutations and combinations, the pigeonhole principle and collisions of short codes

#### [week5#review-week4] Where is the hypothesis used?

*Review · week 4*

**Question:** To prove 1 + 3 + 9 + … + 3ⁿ⁻¹ = (3ⁿ − 1) / 2 by induction, the step for k + 1 must:

- A. check the formula for n = k + 1 by computing both sides for k = 5
- B. assume the formula for k + 1 and simplify
- C. replace the first k terms by (3ᵏ − 1) / 2, add 3ᵏ, and simplify to (3ᵏ⁺¹ − 1) / 2
- D. test the formula for n up to 1,000

### Session 1: Counting arrangements and collisions

#### [week5#s1] Counting arrangements and collisions

*Session 1*

- Count arrangements and selections with the sum and product rules, permutations and combinations
- Compute the chance that short codes collide and verify it by exact enumeration
- Use the pigeonhole principle to show when a collision is certain

#### [week5#sum-product] Multiply for "and then", add for "either, or"

*Block A · two rules*

- **Product rule.** A plate of 3 letters then 4 digits: 26 · 26 · 26 · 10 · 10 · 10 · 10 = 175,760,000 plates.
- **Sum rule.** A PIN of 4, 5 or 6 digits: 10⁴ + 10⁵ + 10⁶ = 1,110,000 PINs. The three lengths never overlap.

> **The sum rule needs disjoint cases.** When cases overlap, subtract what was counted twice: inclusion-exclusion, week 6.

#### [week5#perm-comb] Order matters in an arrangement, not in a selection

*Arrangements and selections*

| Question, from 8 people | Formula | Count |
| --- | --- | --- |
| Chair, deputy and secretary | P(8, 3) = 8 · 7 · 6 | 336 |
| A committee of 3 | C(8, 3) = P(8, 3) / 3! | 56 |
| Why divide by 3! | each committee can be ordered in 3! = 6 ways |  |

P(n, k) = n! / (n − k)! and C(n, k) = n! / (k! (n − k)!).

#### [week5#check-counting] Arrangement or selection?

*Checkpoint*

**Question:** A tasting panel of 4 judges is chosen from 9 cooks; the judges have no roles. How many panels are possible?

- A. 3,024
- B. 126
- C. 6,561
- D. 36

#### [week5#collision-count] All-different assignments are an arrangement count

*Block B · collisions*

- n people, each given one of N codes: **Nⁿ** assignments
- All codes different: **N (N − 1) … (N − n + 1)** = P(N, n)
- Chance all different = P(N, n) / Nⁿ, a count divided by a count

- **Checked by listing.** 6 codes, 3 people: listing all 216 assignments finds 120 with no repeat, and 6 · 5 · 4 = 120. The chance is 120 / 216 = 5/9.

#### [week5#birthday-curve] With 100 codes, 13 people already share one more often than not

*The birthday effect*

| Item | Value |
| --- | --- |
| 5 people | 9.65% |
| 10 people | 37.18% |
| 13 people | 55.72% |
| 20 people | 86.96% |

Exact chance of a shared code among n people with 100 equally likely codes.

#### [week5#expected-pairs] The average number of colliding pairs is C(n, 2) / N

*Pairs*

- Each of the C(n, 2) pairs shares a code in N · Nⁿ⁻² of the Nⁿ assignments
- So, averaged over all assignments, a pair collides 1/N of the time
- 30 people, 100 codes: C(30, 2) / 100 = **4.35** colliding pairs on average

- **A count, not a simulation.** The average is a total over every assignment divided by their number. Brute force on small cases checks it exactly.

#### [week5#check-collision] How many colliding pairs to expect?

*Checkpoint*

**Question:** A shop gives each of 50 loyalty cards a random 3-digit code (1,000 codes). On average over all assignments, how many pairs of cards share a code?

- A. 0.05
- B. 2.45
- C. 50
- D. 1.225

#### [week5#pigeonhole] More items than boxes means some box holds two, and ⌈n / N⌉ is guaranteed

*Block C · pigeonhole*

- 1,000 people and 366 possible birthdays: some day holds at least ⌈1000 / 366⌉ = **3** people
- Proof by contradiction: if every box held at most ⌈n / N⌉ − 1, the boxes would hold fewer than n items
- Below n = N, nothing is guaranteed, though collisions may be likely

- **In hashing.** Any map from long codes to short codes squeezes many inputs into each output: collisions are certain, only their rate is in question.

#### [week5#choosing-length] Choose a code length from the risk you accept, not from the number of people

*Design*

1. **State the risk** "at most 1 in 100 that any two share a code"
2. **Compute exactly** the chance for each length, with the formula
3. **Plan for the rest** a second check when a collision still happens

> **What goes wrong.** "We have 4,000 people and 65,536 codes, so codes are plenty" ignores the pairs. The lab measures how wrong that is.

#### [week5#check-pigeonhole] What is guaranteed?

*Checkpoint*

**Question:** A depot sorts 830 parcels into 100 bays by the last two digits of the parcel number. What does the pigeonhole principle guarantee?

- A. Some bay receives at least 9 parcels
- B. Every bay receives 8 or 9 parcels
- C. Some bay receives at least 8 parcels, and no more is guaranteed
- D. Nothing, since 830 is less than 100 · 100

#### [week5#lab-5-1] Hash collisions and the birthday problem, by formula and by brute force

Lab 5.1 · 105 min

Cut check-in codes from a hash, count collisions two ways, and choose a code length.

[W5_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W5_1.ipynb)

- [ ] Set up; sum and product rules (10 min)
- [ ] Arrangements and selections, two ways (15 min)
- [ ] Short check-in codes from a hash (10 min)
- [ ] Collision-free count: formula and brute force (20 min)
- [ ] The birthday problem exactly, with fractions (15 min)
- [ ] Expected colliding pairs against those issued (15 min)
- [ ] Pigeonhole: when a collision is certain (10 min)
- [ ] Choose the code length and record it (10 min)
- [ ] ✱ Stretch: Count the shared birthdays in the register and compare with the formula

#### [week5#debrief-codes] Four symbols leave 125 colliding pairs; the centre needs eight

*Debrief · lab 5.1*

| k | Codes | Expected pairs | Counted |
| --- | --- | --- | --- |
| 3 | 4,096 | 1,952.6 | 2,026 |
| 4 | 65,536 | 122.0 | 125 |
| 5 | 1,048,576 | 7.6 | 6 |
| 6 | 16,777,216 | 0.5 | 1 |

- Birthdays: 23 people pass one half; four symbols: 302 codes
- k = 2: at least 16 share a code; the largest group found is 27
- 1% risk: k = 8 for 4,000 (0.19%), k = 10 for 40,000

#### [week5#wrap-up] Three things to keep

*Week 5 · wrap-up*

- **Multiply, add, divide.** Product for steps, sum for disjoint cases, divide by the orderings you do not want.
- **Pairs drive collisions.** C(n, 2) / N pairs on average; trouble starts near the square root of N.
- **Check counts by listing.** Brute force on small cases catches the errors a formula hides.

#### [week5#next] Week 6: Counting people: re-identification risk

*Next*

Problem set 5 (60 minutes, AI off for the first attempt): labs/problem-sets/PS5.ipynb.
