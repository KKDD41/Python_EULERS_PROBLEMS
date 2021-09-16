from collections import Counter
from itertools import permutations

def test_on_cube(n):
    return (n**(1/3)).is_integer()

def nl(n): 
    return [int(d) for d in str(n)]

def comprasion(a, b): # сравнение масиивов
    c1 = Counter(nl(a))
    c2 = Counter(nl(b))
    for i in range(0, 10):
        if c1[i] != c2[i]:
            return 0
    return 1

n = 11
print(n)
S = {a**3 for a in range( int((10**n)**(1/3))+1, int((10**(n+1))**(1/3)) )}
while S != set():
    for i in S:
        set_i = set()
        for j in S:
            if comprasion(i, j):
                set_i.add(j)
        if len(set_i)>4:
            print(set_i)
            break
        S = S - set_i

print('stop')