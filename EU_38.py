import math, sys
from itertools import permutations

lst = []

P_0 = []
P = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
for i in P:
    k = list(i)
    P_0.append(k)

for i in range(10, 100):
    S=''
    for j in range(1, 5):
        S = S + str(i*j)
    S = list(map(int, S))
    if S in P_0:
        print(S)

for i in range(101, 1000):
    S=''
    for j in range(1, 4):
        S = S + str(i*j)
    S = list(map(int, S))
    if S in P_0:
        print(S)

for i in range(1001, 10000):
    S=''
    for j in range(1, 3):
        S = S + str(i*j)
    S = list(map(int, S))
    if S in P_0:
        print(S)

print('stopplz')