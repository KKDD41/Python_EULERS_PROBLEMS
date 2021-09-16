import math 

sum=0
for n in range(1, 23):
    i = 1
    while len(str(i**n))<n+1:
        if len(str(i**n)) == n:
            print(i, n, i**n)
            sum +=1
        i+=1

print(sum, 'stop')