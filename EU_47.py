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

def cool(n):
    assert n>0
    Div = []
    for i in range(2, n//2+1):
        if i not in Div and n % i == 0 and p_test(i) == True:
            Div.append(i)
        if len(Div)>4:
            return False
            break
    return True if len(Div) == 4 else False

for n in range(99990, 1000000):
    if cool(n) == True and cool(n+1) == True and cool(n+2)==True:
        print(n, n+1, n+2)

        
print('stop')