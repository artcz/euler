# coding: utf-8

"""
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""

from datetime import datetime
import time


def oneliner():
    """
    TODO: Write a oneliner. Caveat? It will probably be even slower than
    iterations so try running it for smaller number of divisors.
    """
    pass


def solve():
    """
    This implementation took about ~4.5+ hours to come up with the solution.

    Much much faster on pypy.
    """

    def terms(n):
        return sum(range(1, n+1))

    def divisors(n):
        _divisors, i = [], 1
        while i <= n:
            if n % i == 0:
                _divisors.append(i)
            i += 1

        return _divisors

    i = 2
    t = datetime.now()
    while True:
        if len(divisors(terms(i))) > 500:
            return i

        if i % 1000 == 0:
            print i, datetime.now(), datetime.now() - t
            t = datetime.now()
        i += 1


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve)
    print timeit(oneliner)
