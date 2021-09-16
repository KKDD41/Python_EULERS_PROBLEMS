import math 
from fractions import Fraction
from fractions import gcd

def q(n):
    assert n>0
    return 1 if n == 1 else 1+1/(1+q(n-1))

for i in range(1, 999):
    a = Fraction(q(i)).limit_denominator()
    if int(math.log10(a.numerator))>int(math.log10(a.denominator)):
        print(a.limit_denominator())


def solution(N=1000):
  c = 0
  n = d = 1
  for k in range(N):
    n, d = 2 * d + n, d + n
    if int(math.log10(n)) > int(math.log10(d)):
      c+= 1
  return c

print(solution())