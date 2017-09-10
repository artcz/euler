# coding: utf-8

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

"""

import math


four_digit_primes = [
    p
    for p in range(10**3, 10**4)
    if (all(p % j != 0
            for j in range(2, int(math.sqrt(p)) + 1))
        and p >= 2)
]


def are_permutations(a, b, c):
    return set(str(a)) == set(str(b)) == set(str(c))


for n in four_digit_primes:
    i = 3330

    x = n + i
    y = n + 2*i

    if x in four_digit_primes and y in four_digit_primes:
        if are_permutations(n, x, y):
            print "YES, ", n, x, y, " => ", "%d%d%d" % (n, x, y)
