# Lean verification status

`WrightSAT.lean` contains explicit Bool truth-table theorems and a conditional block obstruction. It uses no `sorry`, `axiom`, or Mathlib imports. **Not kernel-checked in this environment** because neither `lean` nor `lake` is installed. Syntax and proof success must be verified by running `lake build` with pinned Lean 4 v4.19.0.

The general theorem about arbitrarily many disjoint copies is justified mathematically in `PAPER.md`; it is not yet formalized as a complete Lean theorem about list-wide single-bit updates. Do not conflate the two.
