import math

def p_test(n): # True, if n is prime 
    assert n>1
    i = 2
    if n == 2:
        return True
    else:
        while i<=int(math.sqrt(n)):
            if n%i == 0:
                return False 
            i+=1
    return True 


for n in range(999, 10000, 2):
    if p_test(n) == False: 
        s = True
        for p in range(2, n):
            q = math.sqrt((n-p)/2)
            if p_test(p) == True and q.is_integer() == True:
                s = s*False
        if s:
            print(n)
    else:
        pass