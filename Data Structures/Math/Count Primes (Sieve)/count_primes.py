class Solution:
    def count_primes(n):
        primes = [1]*n
        primes[0] = primes[1] = 0
        p = 2
        while p * p < n:
            if primes[p]:
                for i in range(p*p, n, p):
                    primes[i] = 0
            p += 1

        return sum(primes)