import math, sys

def Prime(n):
    i = 2
    if n<=1:
        return False
    elif n == 2:
        return True
    else:
        s = True
        while i<=int(math.sqrt(n)):
            if n%i == 0:
                s = False 
            i+=1
        return s

def f(a, b):
    n = 0
    while Prime(n**2+a*n+b):
        n+=1
    return n

M = 0
P = 1
for i in range(-999, 1000):
    for j in range(-1000, 1001):
        if M<f(i, j):
            M = f(i, j)
            P = [i, j]

print(M, P, P[0]*P[1])