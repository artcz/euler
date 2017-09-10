# coding: utf-8

"""


The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""


from collections import deque


def distinct_prime_factors(p):
    factors, i = set(), 2

    while i <= p:
        if p % i == 0:
            factors.add(i)
            p //= i
        else:
            i += 1

    return factors


dpf = distinct_prime_factors

LENGTH = 4
assert LENGTH >= 2


def problem_47():

    i = 1
    consecutive_numbers = deque(maxlen=LENGTH)
    consecutive_numbers.append(i)

    while True:
        i += 1

        consecutive_numbers.append(i)
        # debugging print to show progress
        if i % 1000 == 0:
            print i

        dpfs = [dpf(x) for x in consecutive_numbers]

        if all(len(x) == LENGTH for x in dpfs) and\
           all(d != dpfs[0] for d in dpfs[1:]):

            return "found", consecutive_numbers


print(problem_47())
