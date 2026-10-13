# Ablation matrix

| Model | Permitted operations | Outcome on F_m from all zeros |
|---|---|---|
| Strict 1-flip descent | Only lower unsatisfied-clause count | Trapped immediately |
| Plateau-enabled descent | Allow equal-cost flips | Escape exists (00→10→11 per gadget), but policy-dependent |
| 2-SAT algorithm | Implication graph/SCC | Solves in polynomial time |
| Random restart | Reinitialize and rerun strict descent | Not analyzed for general bounds |
| Arbitrary polynomial SAT algorithm | No locality restriction | No conclusion |

The plateau is an **algorithmic** obstruction, not a complexity-class separation.
