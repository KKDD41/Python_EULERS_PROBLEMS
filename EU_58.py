import math, sys 
from fractions import Fraction
from collections import defaultdict
from functools import reduce


def is_prime(n): # True, if n is prime 
    assert n>0 
    i = 2
    if n ==1:
        return 0
    if n == 2:
        return 1
    else:
        while i<=int(math.sqrt(n)):
            if n%i == 0:
                return 0 
            i+=1
    return 1
        
def spiral_diagonals():
    n = 1
    step = 2
    since_last = 0
    while True:
        yield n
        n += step
        since_last += 1
        if since_last == 4:
            step += 2
            since_last = 0

def main():
    level = 0
    primes = 0
    for i, n in enumerate(spiral_diagonals()):
        if (i-1) % 4 == 0:
            level += 1
        if is_prime(n):
            primes += 1
        side_length = (2 * level) + 1
        ratio =  float(primes) / float(i+1)
        if 0 < ratio < 0.1:
            print(side_length)
            return

if __name__ == "__main__":
    main()

#print(spiral_diagonals())