import math
from itertools import permutations

def sq(n, Q):
    return int(Q[0]*(n**2)+Q[1]*n)

def reshi(a, b, c):
    x_2 = ( -b + math.sqrt(b**2-4*a*c) )/(2*a)
    return int(x_2)

def set_of_num(i):
    assert i<6, -1<i
    P = [[1/2,1/2], [1,0], [3/2,-1/2], [2,-1], [5/2,-3/2], [3,-2]]
    P.reverse()
    lower_bound = [19, 21, 23, 26, 32, 45]
    upper_bound = [59, 64, 71, 82, 101, 141]
    return [sq(n, P[i]) for n in range(lower_bound[i], upper_bound[i])]

def app_num(n, i):
    S = []
    for m in set_of_num(i+1):
        if m//100 == n%100:
            S.append(m)
    return S

for p in permutations([0, 1, 2, 3, 4]):
    p = list(p) # да это 6 циклов в цикле и че ты мне сделаешь
    for a in set_of_num(0): # без мата
        for b in app_num(a, p[0]): # но эта задача пиздата
            for c in app_num(b, p[1]): # а твоя мама все равно толстая
                for d in app_num(c, p[2]):
                    for e in app_num(d, p[3]):
                        for f in app_num(e, p[4]):
                            if f%100 == a//100:
                                print(sum([a, b, c, d, e, f]))

print('stop') 