import math, sys

def fif(n: str):
    N= list(map(int, list(n)))
    s = 0
    for i in range(len(N)):
        s = s + (N[i])**5
    return s if int(n) == s else 0

sum = 0
for i in range(10**6):
    i = str(i)
    if fif(i) != 0:
        print(fif(i))
    sum+= fif(i)

print(sum)