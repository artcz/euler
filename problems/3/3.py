# coding: utf-8

"""
To run:
    python2.7 3.py

Problem:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""

import math
import time

NUMBER = 600851475143


def oneliner():
    """
    This will "loop" until sqrt(N), which in this case is significantly more
    iterations than required to find highest prime factor;
    TBD: how to stop reduce mid way(?)
    """
    # Protip: can rewrite lambda below as a one-liner regular function, can add
    # debugging information (like print n, i) before return, which makes it
    # easier to debug.
    return max(reduce(
        lambda n, i: [
            (n[0] / i), n[1] + [i]
        ] if n[0] % i == 0 else [n[0], n[1]],
        xrange(2, int(math.sqrt(NUMBER))),
        [NUMBER, []],
    )[1])


def solve():
    def factors(n):
        """
        This implementation goes from 0 to the highest prime factor, in this
        case causing 6857 iterations of the loop
        """
        _factors, i = [], 2
        while i <= n:
            if n % i == 0:
                _factors.append(i)
                n /= i
            i += 1

        return max(_factors)

    return factors(NUMBER)


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1
    print timeit(solve)
    print timeit(oneliner)
