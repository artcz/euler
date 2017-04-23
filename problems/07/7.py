# coding: utf-8

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""


import itertools
import math
import time


def oneliner():
    # Fun fact, this 'oneliner' with names for lambdas is
    # half-an-order-of-magnitude slower than the actual oneliner that does
    # pretty much the same thing but in actual one line. shrug.jpg
    #
    # is_prime = lambda n: all(
    #     [n % j != 0
    #      for j in range(2, int(math.sqrt(n))+1)]
    # )
    # infinite_primes = (
    #     p for p in itertools.count()
    #     if is_prime(p) and p >= 2
    # )
    # return list(
    #     itertools.takewhile(
    #         lambda x: x[0] <= 10001, enumerate(infinite_primes, 1)
    #     )
    # )[-1]

    return list(
        itertools.takewhile(
            lambda x: x[0] <= 10001, enumerate(
                (p for p in itertools.count()
                if (all(p % j != 0
                       for j in range(2, int(math.sqrt(p))+1))
                    and p >= 2)),
                1  # start enumerating from 1.
            )
        )
    )[-1]


def solve():
    prime_counter, number = 0, 2
    while True:

        for j in range(2, int(math.sqrt(number))+1):
            if number % j == 0:
                break
        else:
            prime_counter += 1
            if prime_counter == 10001:
                return prime_counter, number

        number += 1


if __name__ == "__main__":
    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve)
    print timeit(oneliner)
