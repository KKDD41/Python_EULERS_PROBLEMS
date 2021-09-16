import math, sys

def turn(n):
     t= str(n)
     return int(t[::-1])

def pal_test(n):
    return True if n == turn(n) else False

def Lycher(n):
    g = n
    for i in range(1, 51):
        m = g + turn(g)
        if pal_test(m):
            return False
            break
        else:
            g = m
    return True

K = 0
for n in range(10000):
    if Lycher(n):
        K +=1
print(K)