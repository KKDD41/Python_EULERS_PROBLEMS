import numpy as np


def factorize(p, primes, cache):  # возвращает все возможные разложения на множители числа p
    if p in primes:
        cache[p] = {(p,)}
        return cache[p]
    ways = cache.get(p, set())
    if len(ways):
        return ways
    for i in range(2, int(np.sqrt(p)) + 1):
        q, r = divmod(p, i)
        if r == 0:
            part1 = factorize(i, primes, cache)
            part2 = factorize(q, primes, cache)
            for p1 in part1:
                for p2 in part2:
                    tmp = list(p1 + p2)
                    tmp.sort()
                    ways.add(tuple(tmp))
    ways.add((p,))
    cache[p] = ways
    return ways


def find_all_primes(maxnum): # лол по сути це решето эратосфена
    primes = np.arange(1, maxnum + 1)
    Bool = np.ones(maxnum, dtype=bool)
    Bool[0] = 0
    maxiter = int(np.sqrt(maxnum))
    for i in range(2, maxiter + 1):
        if Bool[i - 1]:
            Bool[np.arange(2 * i - 1, maxnum, i)] = False
    return primes[Bool]


def worker(max_k):
    primes = set(find_all_primes(2 * max_k))
    cache = {}
    pairs = {}
    for num in range(4, 2 * max_k + 1):
        ways = factorize(num, primes, cache)
        for w in ways:
            if len(w) > 1:
                k = num - sum(w) + len(w)
                if k <= max_k:
                    pairs.setdefault(k, num)
    res = sum(set(pairs.values()))
    return res, pairs


if __name__ == '__main__':
    res, pairs = worker(12000)
    print(res, pairs)