import math, sys
S = []
for b in range(1, 10):
    for a in range(1, 10):
        for c in range(1, 10):
            if c*(9*a+b) == 10*a*b and a!=c:
                S.append(str(a)+str(b)+'/'+str(b)+str(c))

print(S)