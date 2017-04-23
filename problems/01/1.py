# coding: utf-8

"""
To run:
    python2.7 1.py

Problem:
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

def oneliner():
    return sum(
        i for i in range(1000)
        if i % 3 == 0 or i % 5 == 0
    )


def impl1():
    numbers = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)

    return sum(numbers)

def impl2():
    j = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            j += i

    return j

if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(impl1)
    print timeit(impl2)
    print timeit(oneliner)
