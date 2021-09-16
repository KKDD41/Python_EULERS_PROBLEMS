import math

def lst(a, b): #list of primes 
    assert b+1>a>2
    p = []
    for n in range(a, b+1):
        p.append(n)
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                p.pop()
                break
            else:
                pass
    return p 

def Num(k):
    e = list(map(int, str(k)))
    return e

def W(A, B, C):
    s = True
    for i in range(10):
        if A.count(i) != B.count(i) or A.count(i) != C.count(i) or B.count(i) != C.count(i):
            s = False
    return s


L = lst(1000, 9999)

for i in range( len(L) ):
    for j in range(i+1, len(L)):
        diff=L[j]-L[i]
        if L[j]+diff in L and W( Num(L[i]), Num(L[j]), Num(L[j]+diff) ):
            print(L[i], L[j], L[j]+diff)




