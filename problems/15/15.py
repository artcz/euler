# coding: utf-8

"""
Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

￼
How many such routes are there through a 20×20 grid?
"""

from math import factorial
import time


def oneliner():
    pass


def solve():
    """
    Based on this:
        http://mathworld.wolfram.com/LatticePath.html

    And this:
        http://mathworld.wolfram.com/BinomialCoefficient.html
    """
    def binomial_formula(n, k):
        return factorial(n) / (factorial(n-k) * factorial(k))

    # Grid is 20, 20 so
    return binomial_formula(20+20, 20)


if __name__ == "__main__":
    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve)
    print timeit(oneliner)
