import math, sys
from copy import deepcopy
from itertools import permutations

D = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 3))
D_0 = []
for d in D:
    D_0.append(list(d))

def ADD(d, i):
    assert i<7
    if len(d)<3:
        return []
    p = [2, 3, 5, 7, 11, 13, 17]
    S = []
    q = (-100*d[len(d)-2]-10*d[len(d)-1]) % p[i]
    if q>9:
        return []
    else:
        while q<10:
            d_0 = deepcopy(d)
            d_0.append(q)
            S.append(d_0)
            q+=p[i]
        return S # vozvraschaet list podhodyaschih perestanovok dliny len(d)+1


Q = [D_0, [], [], [], [], [], [], []]
for i in range(7):
    for d in Q[i]:
        Q[i+1] = Q[i+1]+ADD(d, i)
sum = 0
for k in Q[7]:
    if k.count(0)==1 and k.count(1)==1 and k.count(2)==1 and k.count(3)==1 and k.count(4)==1 and k.count(5)==1 and k.count(6)==1 and k.count(7)==1 and k.count(8)==1 and k.count(9):
        pp = int( str(k[0])+str(k[1])+str(k[2])+str(k[3])+str(k[4])+str(k[5])+str(k[6])+str(k[7])+str(k[8])+str(k[9]) )
        print(pp)
        sum+=pp
print(sum)

