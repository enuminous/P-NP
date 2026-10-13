import unittest
from experiment import clauses, unsat, strict_descent, run

class AuditTests(unittest.TestCase):
    def test_unique_solution(self):
        for n in range(2,12,2):
            cnf=clauses(n)
            self.assertEqual([a for a in range(1<<n) if unsat(a,cnf)==0],[(1<<n)-1])
    def test_strict_descent_stuck(self):
        for n in range(2,12,2):
            a,s,c=strict_descent(0,clauses(n),n)
            self.assertEqual((a,s,c),(0,0,n//2))
    def test_one_flip_plateau(self):
        for n in range(2,12,2):
            cnf=clauses(n)
            self.assertTrue(all(unsat(1<<i,cnf)==n//2 for i in range(n)))
    def test_counterexample_escape(self):
        # A plateau move from 00 to 10 followed by 11 solves one gadget.
        cnf=clauses(2)
        self.assertEqual([unsat(a,cnf) for a in [0,1,3]],[1,1,0])
    def test_results(self):
        self.assertEqual(len(run(10)),5)

if __name__=='__main__': unittest.main()
