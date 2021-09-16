import math 
from fractions import Fraction


a = [2,1,2,1,1,4,1,1,6,1,1,8,1,1,10,1,1,12,1,1,14,1,1,16,1,1,18,1,1,20,1,1,22,1,1,24,1,1,26,1,1,28,1,1, 30,1,1,32,1,1,34,1,1,36,1,1,38,1,1,40,1,1,42,1,1, 44,1,1,46,1,1,48,1,1,50,1,1,52,1,1,54,1,1,56,1,1, 58,1,1,60,1,1,62,1,1,64,1,1,66, 1]
print(len(a))

a.reverse()
f = []
x = a[0]
f.append(x)
for i in range(99):
    x = Fraction(a[i+1]+ Fraction(1, f[i]))
    x.limit_denominator()
    f.append(x)
p = str(f[99].numerator)
sum = 0
for i in range(len(p)):
    sum+=int(p[i])

print(sum)


