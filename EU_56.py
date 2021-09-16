import math, sys

def digit_sum(n):
    return sum( list(map(int, str(n))) )

m = 1
for i in range(1, 100):
    for j in range(1, 100):
        m = max(m, digit_sum(i**j))

print(m)
