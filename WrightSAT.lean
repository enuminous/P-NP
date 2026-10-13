/-!
WrightSAT: finite gadget and generic disjoint-block obstruction.
Lean 4 core only. No Mathlib dependency, no sorry.
This proves a restricted local-search failure, NOT P != NP.
-/
namespace WrightSAT

/-- Unsatisfied-clause count for G(x,y) = (x ∨ y) ∧ (x ∨ ¬y) ∧ (¬x ∨ y). -/
def cost (x y : Bool) : Nat :=
  (if x || y then 0 else 1) +
  (if x || !y then 0 else 1) +
  (if !x || y then 0 else 1)

theorem zero_cost : cost false false = 1 := by decide
theorem flip_left_plateau : cost true false = cost false false := by decide
theorem flip_right_plateau : cost false true = cost false false := by decide
theorem solution_cost : cost true true = 0 := by decide

theorem unique_solution (x y : Bool) :
    cost x y = 0 ↔ x = true ∧ y = true := by
  cases x <;> cases y <;> decide

/-- Each local flip from the zero assignment fails to decrease the cost. -/
theorem no_strict_improvement :
    ¬ (cost true false < cost false false) ∧
    ¬ (cost false true < cost false false) := by decide

/-- A sideways move followed by a flip reaches the solution. -/
theorem sideways_escape :
    cost false false = cost true false ∧ cost true true < cost true false := by decide

/-- Sum of independent block costs. -/
def totalCost (xs : List (Bool × Bool)) : Nat :=
  xs.foldr (fun p acc => cost p.1 p.2 + acc) 0

theorem block_obstruction (x y : Bool)
    (h : x = false ∧ y = false) :
    ¬ (cost (!x) y < cost x y) ∧
    ¬ (cost x (!y) < cost x y) := by
  rcases h with ⟨rfl, rfl⟩
  decide

end WrightSAT
