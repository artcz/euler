
import math


def is_prime(p):
    return (all(p % j != 0
                for j in range(2, int(math.sqrt(p)) + 1))
            and p >= 2)


base_primes = [
    p
    for p in range(2, 4000)
    if is_prime(p)
]


longest = 0

for j, p in enumerate(base_primes):
    for i in range(0, j):
        s = sum(base_primes[i:j])
        if is_prime(s) and s < 1e6:
            longest = max(longest, len(base_primes[i:j]))
            if longest == len(base_primes[i:j]):
                print s, len(base_primes[i:j])
