import math, sys


w = 200

def f(w, x):
    assert w>=0
    V = [1, 2, 5 ,10, 20, 50, 100, 200]
    if w == 0:
        return 1
    else:
        F = 0
        for i in V:
            if i <= x and w-i>=0:
                F+=f(w-i, i)
    return F

print(f(200, 200))

