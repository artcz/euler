# coding: utf-8

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""


import math
import time


def oneliner():
    """
    TODO: write oneliner version of this challange.
    """
    pass


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
