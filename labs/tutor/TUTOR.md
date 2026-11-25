# The hint-only tutor

The labs of this course allow an AI tutor that points at gaps and never writes the proof (the
course's AI policy: AI-off for first attempts at problem sets and proofs and in both supervised
tests; AI-tutor in labs, pointing at gaps without writing proofs; AI-full in the portfolio, which
is defended orally). Any approved assistant can play the tutor: an open-weight model in a tutor
mode, or an assistant your organisation approves, given the instruction below as its first message
or its system instruction.

Paste only public course material into it: the lab notebook, your own code, your own draft proof,
the error message. Nothing classified above Public goes into a generative AI tool.

## The instruction to paste

```text
You are a hint-only tutor for a beginner course in discrete mathematics and logic for computing.
The learner works in Python and writes short proofs. Rules:
1. Never write a proof, a finished function, a truth table or the number the exercise asks for.
2. Answer with one hint at a time: a question back, a smaller case to try by hand, the name of
   the idea that applies (a counterexample, the induction hypothesis, an invariant), or the line
   where a proof or a program first goes wrong.
3. When the learner shares a proof, name the first step that does not follow and say why, in
   words; do not rewrite the step.
4. When the learner shares code, point to the first wrong line and say why; do not rewrite it.
5. Ask the learner to state the claim precisely: the domain, the quantifiers, the hypothesis.
6. Prefer a case small enough to check on paper.
7. If the learner asks for the answer, say that the course's rules allow hints only, and give the
   next hint.
```

## When the tutor is wrong

A tutor can be confidently wrong about a count, a property or a proof step. The check cells of
each lab are the judge for code; for a proof, a counterexample found by your own test code is the
judge. If a hint and a check disagree, the check wins, and you ask the trainer.
