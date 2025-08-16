## Key Observation

- Start from the prime number 2 and go through all its multiples 
- Progress to the next available prime number (primes[p] == True) and do the same
- Each time, checking if p*p is available.


##### Why P * P instead of P + P
If you start crossing off multiples at p + p (2p), you will cross off numbers like 2p, 3p, …, but notice:

2p was already crossed off when you processed 2.

3p was already crossed off when you processed 3 (if 3 < p).

In fact, every multiple of p less than p * p has already been eliminated by a smaller prime factor.