import math, sys
from itertools import permutations


L = set()
for P in list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)):
    if P[0]*(P[1]*1000+P[2]*100+P[3]*10+P[4]) == P[5]*1000+P[6]*100+P[7]*10+P[8] or (P[0]*10+P[1])*(P[2]*100+P[3]*10+P[4]) == P[5]*1000+P[6]*100+P[7]*10+P[8]:
        L.add(P[5]*1000+P[6]*100+P[7]*10+P[8])

print(sum(L), L)
