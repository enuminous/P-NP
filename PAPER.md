# Recursive Refinement and the Limits of Strict Local SAT Search

**Matthew Chenoweth Wright; mathematical audit and computational implementation with AI assistance**  
October 13, 2026

## Abstract

We audit the January 23, 2025 article *A Formal Argument for P ≠ NP Using Asymptotic Analysis and Computational Limits*. Its asymptotic comparison correctly observes exponential dominance over polynomial growth but does not establish exponential lower bounds for NP-complete problems. We replace the unsupported inference with a rigorous conditional theorem: strict single-variable-flip descent on the unsatisfied-clause count can terminate at a non-satisfying local minimum on a family of satisfiable 2-CNF formulas. We prove this family analytically and verify it by exhaustive enumeration through 16 variables. The family is efficiently solvable by 2-SAT algorithms and therefore is explicitly **not** evidence of P ≠ NP. The result is a limitation of a particular local search rule, not a general complexity lower bound.

## 1. Original argument: valid and invalid steps

For fixed k, 2^n/n^k diverges to infinity. But this compares **selected algorithms**, not an upper bound on the fastest possible algorithm. Big-O upper bounds on known exponential algorithms do not yield lower bounds on every possible algorithm. NP-completeness of decision SAT does not itself establish superpolynomial complexity. Gödel incompleteness and Heisenberg uncertainty do not supply the missing lower bound. Approximation guarantees (e.g. Christofides for metric TSP) do not imply exact solutions can never be produced.

## 2. Definitions

For CNF F and assignment a, let U_F(a) be the number of unsatisfied clauses. A *strict 1-flip descent solver* starts at a specified assignment and repeatedly changes exactly one variable **only if** that move strictly decreases U_F. It stops otherwise. Tie-breaking among strictly improving moves is arbitrary. This theorem concerns this algorithm family and initial assignment, not all local-search methods.

## 3. Construction and theorem

For Boolean variables x,y, define

G(x,y)=(x OR y) AND (x OR NOT y) AND (NOT x OR y).

Truth table:

| x | y | Unsatisfied clauses |
|---|---|---|
| 0 | 0 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

For m >= 1, define F_m as the conjunction of m disjoint copies G(x_i,y_i). It has n=2m variables and 3m clauses.

**Theorem.** F_m has exactly one satisfying assignment, the all-ones assignment. At the all-zeros assignment a_0, U_Fm(a_0)=m and every Hamming-distance-one neighbor a' has U_Fm(a')=m. Consequently, any strict 1-flip descent solver initialized at a_0 stops immediately without finding a satisfying assignment.

**Proof.** Each gadget has exactly one satisfying assignment, (1,1), by the truth table. Disjoint conjunction gives a unique all-ones satisfying assignment. At all zeros each gadget contributes one violated clause, giving m. A single flip changes only one gadget from (0,0) to either (1,0) or (0,1); both have exactly one violated clause. All other gadgets remain unchanged, so U_Fm stays m. No strict improvement exists. QED.

**Important counterexample to overclaiming.** The family consists of 2-CNF formulas, solvable in polynomial time by standard 2-SAT algorithms. A solver allowing sideways moves can escape each gadget in two flips (00 -> 10 -> 11). The result is therefore a heuristic failure, not inherent NP-complete hardness.

## 4. Computational validation

`experiment.py` enumerates every assignment for n = 2,4,...,16, checks the unique satisfying assignment, verifies the local plateau, and writes `results.csv`. Five automated tests check the theorem's properties and the sideways-move counterexample. These finite checks supplement but do not replace the general analytic proof.

## 5. Adversarial Zoo-style gates

- TORTOISE / anti-circularity: PASS for the restricted theorem; no assumed exponential SAT lower bound.
- Formal definitions: PASS for the explicit strict-descent algorithm and family.
- Counterexample: PASS; 2-SAT tractability and plateau escape prevent universal extrapolation.
- Dimensions: Not applicable (discrete complexity theory).
- Asymptotic inference: ORIGINAL ARGUMENT FAILS; a worst-case bound on one heuristic is not a lower bound for all algorithms.
- Proof check: HAND PROOF plus finite exhaustive tests; no Lean kernel certificate.
- Novelty: NOT ESTABLISHED; local minima for SAT heuristics are a familiar phenomenon.
- Millennium problem: NOT SOLVED.

This is a targeted adversarial review, not execution of the entire Monolithic Zoo implementation.

## 6. Ablations

A0: strict-improvement 1-flip from all zeros: fails immediately.

A1: allow non-worsening (sideways) moves with a suitable policy: can reach all ones; no unconditional success guarantee from sideways moves alone.

A2: use a conventional 2-SAT implication-graph algorithm: polynomial-time decision and witness construction.

A3: random restarts: can change empirical success but no bound is established by this study.

A4: general SAT solvers (CDCL, resolution, etc.): outside the theorem's scope.

## 7. Relation to P vs NP barriers

To prove P != NP one must rule out **all** polynomial-time deterministic algorithms for at least one NP problem. Relativization (Baker–Gill–Solovay), natural proofs (Razborov–Rudich), and algebrization (Aaronson–Wigderson) are barriers that broad approaches must address. None is overcome here.

## 8. Next research direction

Formalize a nontrivial class of recursive refinement solvers, identify the weakest sufficient assumptions for a lower bound, and test counterexamples that relax locality, monotonicity, memory, restarts and branching. Prefer a theorem about a precisely stated restricted class over an unsupported global complexity claim. Then pursue Lean verification of the theorem, preserving the distinction between verified mathematics and empirical evidence.
