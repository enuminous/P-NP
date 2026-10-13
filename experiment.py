"""Exact exhaustive experiment on satisfiable SAT traps for strict 1-flip descent."""
import argparse, csv
from pathlib import Path

def clauses(n):
    # each pair (x,y): (x or y) & (x or not y) & (not x or y)
    assert n % 2 == 0 and n >= 2
    return [(i+1,i+2) for i in range(0,n,2)] + [(i+1,-(i+2)) for i in range(0,n,2)] + [(-(i+1),i+2) for i in range(0,n,2)]

def unsat(assignment, cnf):
    return sum(not any(bool(assignment & (1 << (abs(l)-1))) == (l > 0) for l in c) for c in cnf)

def strict_descent(assignment, cnf, n):
    steps = 0
    while True:
        cost = unsat(assignment,cnf)
        neighbors = [(unsat(assignment ^ (1<<i),cnf),i) for i in range(n)]
        best, bit = min(neighbors)
        if best >= cost: return assignment, steps, cost
        assignment ^= 1<<bit
        steps += 1

def run(max_n=16):
    results=[]
    for n in range(2,max_n+1,2):
        cnf=clauses(n)
        start=0
        final,steps,cost=strict_descent(start,cnf,n)
        sat=sum(unsat(a,cnf)==0 for a in range(1<<n))
        oneflip=min(unsat(1<<i,cnf) for i in range(n))
        # no strict improvement from zero; global solution all ones
        assert cost==n//2 and steps==0 and oneflip==cost
        assert unsat((1<<n)-1,cnf)==0
        assert sat==1
        results.append(dict(variables=n,clauses=len(cnf),assignments=1<<n,satisfying=sat,initial_unsatisfied=n//2,best_oneflip=oneflip,strict_descent_steps=steps,final_unsatisfied=cost))
    return results

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-n',type=int,default=16)
    args=parser.parse_args()
    rows=run(args.max_n)
    path=Path(__file__).with_name('results.csv')
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    for r in rows: print(r)
    print('Wrote',path)
