# coding: utf-8

"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1²
15 = 7 + 2×2²
21 = 3 + 2×3³
25 = 7 + 2×3³
27 = 19 + 2×2³
33 = 31 + 2×1³

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

from math import sqrt


def is_prime(p, primes):
    for i in primes:
        if i > sqrt(p):
            break

        if p % i == 0:
            return False

    return True


def problem_46():

    primes = [2, 3, 5, 7]

    i = 9    # 9 is the first ood composite
    while True:
        # we don't need to check even numbers
        i += 2

        # debugging print to show progress
        if i % 100000 == 3:
            print i

        if is_prime(i, primes):
            primes.append(i)

        conjecture_holds = False
        for p in primes:
            foo = sqrt((i - p) / 2)
            if foo == int(foo):
                conjecture_holds = True
                break

        if not conjecture_holds:
            return i


print(problem_46())
