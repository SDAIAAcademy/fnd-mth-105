---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
deck: "week4"
day: 4
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/slides/week4.html"
---

# Discrete Mathematics and Logic for Computing

## Week 4: Induction, invariants and the limits of testing

Claims that pass every test you ran, and the proofs that cover the cases you did not

#### [week4#title] Induction, invariants and the limits of testing

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 4: Claims that pass every test you ran, and the proofs that cover the cases you did not

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week4#agenda] Induction, invariants and the limits of testing

*This week*

- **Session 1 · Induction, invariants, testing and proof**: Mathematical and structural induction, loop invariants, and why a claim tested on many cases is not proved

#### [week4#review-week3] Which property fails?

*Review · week 3*

**Question:** On the files of a shared drive, "file A is in the same folder as file B or in one of its subfolders" relates A to B. Which property does it lack?

- A. Reflexivity
- B. Transitivity
- C. It has all four, so it is an equivalence
- D. Symmetry

### Session 1: Induction, invariants, testing and proof

#### [week4#s1] Induction, invariants, testing and proof

*Session 1*

- Prove a claim about the integers by mathematical induction after testing it in code
- Prove a property of a recursive structure by structural induction
- State and check a loop invariant, and use it to prove a loop correct

#### [week4#induction-shape] Induction proves a claim for every n with two finite pieces of work

*Block A · induction*

1. **Base** show P(1), or P of the first value
2. **Hypothesis** assume P(k) for one k ≥ 1
3. **Step** show P(k + 1), using P(k)

- Base and step together reach every n: P(1), so P(2), so P(3), and so on
- Without the base, the step proves nothing; without the step, the base proves one case

#### [week4#induction-example] Test it, then prove it: 1 + 2 + … + n = n(n + 1) / 2

*Worked example*

```python
# file: python
all(sum(range(1, n + 1)) == n * (n + 1) // 2
    for n in range(1, 5001))   # True
```

1. **Base.** n = 1: 1 = 1 · 2 / 2
2. **Hypothesis.** 1 + … + k = k(k + 1) / 2
3. **Step.** 1 + … + k + (k + 1) = k(k + 1) / 2 + (k + 1) = (k + 1)(k + 2) / 2, using the hypothesis for the first k terms ∎

#### [week4#strong-induction] Strong induction may assume the claim for every value below k + 1

*Strong induction*

**Claim.** Every integer n ≥ 2 is a product of primes.

- If n is prime, it is a product of one prime
- Otherwise n = a · b with 2 ≤ a, b < n
- By the hypothesis for a and for b, both are products of primes, so n is too ∎

- **When to use it.** When the step needs a smaller case that is not k itself: a factor, half of n, a subtree. Recursive code that splits its input is proved this way.

#### [week4#check-induction-parts] What is missing?

*Checkpoint*

**Question:** A proof that "n + 1 < n for every n ≥ 1" assumes k + 1 < k and adds 1 to both sides to get k + 2 < k + 1. What is wrong with it?

- A. It has no base case, and the base case is false
- B. Adding 1 to both sides is not allowed
- C. The hypothesis assumes what it wants to prove
- D. It needs strong induction instead

#### [week4#structural] Structural induction follows the way a structure is built

*Block B · structural induction*

- **A recursive definition.** A nested list is either a number, or a list of nested lists. A tree is a node with a list of subtrees.
- **Its induction.** Prove the claim for the smallest pieces, then show that building from pieces that satisfy it gives a whole that satisfies it.

> **No n needed.** The induction is on the structure itself; each recursive call works on a smaller part.

#### [week4#structural-example] In a tree where every node has 0 or 2 children, leaves = inner nodes + 1

*Worked example*

- **Base.** A single node: 1 leaf, 0 inner nodes
- **Step.** A root with subtrees L and R that satisfy it: leaves = (inner(L) + 1) + (inner(R) + 1) = (inner(L) + inner(R) + 1) + 1
- The root is the one new inner node, so leaves = inner + 1 ∎

```python
# file: python
def leaves(t):
    if not t["children"]:
        return 1
    return sum(leaves(c) for c in t["children"])
```

#### [week4#recursion-correct] A recursive function is proved correct by induction on the size of its input

*Recursive code*

```python
# file: python
def total(xs):
    if not xs:
        return 0
    return xs[0] + total(xs[1:])
```

1. **Base.** The empty list returns 0, its sum
2. **Hypothesis.** total is right on lists of length k
3. **Step.** On length k + 1 it returns xs[0] plus the sum of the rest, by the hypothesis: the sum ∎

#### [week4#check-structural] What may the step assume?

*Checkpoint*

**Question:** To prove by structural induction that a recursive depth function on nested lists is correct, the step for a list [a, b, c] may assume:

- A. that the function is correct on [a, b, c]
- B. that it is correct on a only
- C. that it is correct on each of a, b and c
- D. that it is correct on every list of length 2

#### [week4#invariants] An invariant is true before the loop and after every pass

*Block C · loop invariants*

```python
# file: python
total, i = 0, 0
while i < len(xs):
    # invariant: total == sum(xs[:i])
    total += xs[i]
    i += 1
```

| Part | Show |
| --- | --- |
| Initialisation | true before the first pass |
| Maintenance | a pass keeps it true |
| Termination | the loop stops |
| At exit | invariant and exit condition give the result |

#### [week4#testing-vs-proof] A pattern can hold for every case you tried and still break

*The gap*

| Points on a circle | Regions |
| --- | --- |
| 1 | 1 |
| 2 | 2 |
| 3 | 4 |
| 4 | 8 |
| 5 | 16 |
| 6 | 31 |

- Join every pair of points with a chord, no three chords meeting inside
- The first five suggest 2ⁿ⁻¹; the sixth gives **31**, not 32
- A test can refute a pattern; only a proof can confirm it

#### [week4#what-tests-give] Generated tests find counterexamples cheaply, so run them before you prove

*Using tests well*

- **Many cases.** Every n up to a bound, or random inputs. Cheap evidence and a fast way to find a false claim.
- **Edge cases.** Zero, one, the empty list, equal values, the first case where a pattern could change.
- **Their limit.** Write what the tests cover: "n from 1 to 1,000, no counterexample". Never write "true".

#### [week4#check-invariant] Which statement is an invariant?

*Checkpoint*

**Question:** A loop counts the even numbers in a list: count starts at 0, i at 0; each pass adds 1 to count if xs[i] is even, then adds 1 to i. Which invariant proves it correct?

- A. count ≥ 0
- B. count equals the number of evens in the whole list
- C. count = i
- D. count equals the number of evens in xs[:i]

#### [week4#lab-4-1] Claims tested in code, then proved

Lab 4.1 · 105 min

An added lab: test claims on generated cases, prove them by induction and invariants, and find the gap in a flawed proof.

[W4_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W4_1.ipynb)

- [ ] Set up; test a sum formula on many cases (10 min)
- [ ] Prove it by induction (15 min)
- [ ] True for forty cases, false on the next (10 min)
- [ ] Structural induction on the team tree (20 min)
- [ ] Loop invariants asserted in code (20 min)
- [ ] Find the gap in a flawed proof (15 min)
- [ ] Record which claims are proved (15 min)
- [ ] ✱ Stretch: Prove an invariant for binary search over the volunteer codes

#### [week4#debrief-claims] Forty passes did not make claim B true, and one hidden assumption broke a proof

*Debrief · lab 4.1*

| Claim | Status |
| --- | --- |
| Sum of first n odd numbers is n² | tested to 1,000, proved |
| n² + n + 41 is prime | passes n = 0 to 39; at 40: 1,681 = 41 · 41 |
| Edges = nodes − 1 | team tree 25 and 24; 500 trees; proved |
| divide(a, b) | 2,000 pairs; proved from its invariant |
| 2ⁿ ≥ n² for n ≥ 1 | fails at n = 3; step needs k ≥ 3 |

- The flawed step used k² ≥ 2k + 1, false for k = 1 and 2
- Repaired: 2ⁿ ≥ n² for every n ≥ 4

#### [week4#wrap-up] Three things to keep

*Week 4 · wrap-up*

- **Base, hypothesis, step.** Say where the step uses the hypothesis. A step alone proves nothing.
- **Induction follows structure.** Integers, lists, trees and loops: the proof follows the way the thing is built.
- **Tests refute, proofs confirm.** Write what your tests cover, never "true", until the proof exists.

#### [week4#next] Week 5: Counting, collisions and the birthday problem

*Next*

Problem set 4 (60 minutes, AI off for the first attempt): labs/problem-sets/PS4.ipynb. Then the first supervised test, on weeks 1 to 4.
