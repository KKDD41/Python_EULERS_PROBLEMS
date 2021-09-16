import math, sys

a, b = 0, 1
i = 1
while int(math.log10(b)+1)<1000:
    a, b = b, a+b
    i+=1
print(i)   
