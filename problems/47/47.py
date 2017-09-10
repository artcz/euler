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


def problem_47():

    i = 10
    consecutive_numbers = deque(maxlen=LENGTH)
    consecutive_numbers.append(i)
    while True:
        i += 1

        consecutive_numbers.append(i)
        # debugging print to show progress
        if i % 1000 == 0:
            print i

        c = consecutive_numbers

        try:
            c_0 = dpf(c[0])
            c_1 = dpf(c[1])
            c_2 = dpf(c[2])
            c_3 = dpf(c[3])

            if len(c_0) == 4 and len(c_1) == 4 and len(c_2) == 4\
               and len(c_3) == 4\
               and c_0 != c_1 != c_2 != c_3:

                return "found", c[0], c[1], c[2], c[3]
        except IndexError:
            pass


print(problem_47())
