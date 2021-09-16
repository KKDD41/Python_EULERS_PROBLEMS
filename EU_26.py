import math, sys

# funnction for GCD 
def GCD (a, b ) : 
    if (b == 0 ) : 
        return a 
    return GCD( b, a % b )  
  
# Fucnction return smallest + ve 
# integer that holds condition  
# A ^ k(mod N ) = 1 

def ord(A, N): 
    if (GCD(A, N ) != 1) : 
        return -1  # result store power of A that rised  # to the power N-1 
    result = 1
    K = 1
    while (K < N) :   # modular arithmetic 
        result = (result * A) % N   # return samllest + ve integer 
        if (result == 1) : 
            return K    # increment power 
        K += 1
    return -1

print(ord(10, 983))

num = 0
s = -1
for i in range(1000):
    if ord(10, i)==982:
        print(i)
