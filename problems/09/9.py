# coding: utf-8

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²

For example, 3³ + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time


def oneliner():

    return [(a, b, c, a * b * c)
            for c in range(5, 500)
            for b in range(1, c)
            for a in range(1, b)
            if a + b + c == 1000 and a**2 + b**2 == c**2][0]


def solve1():

    for c in range(5, 500):
        for b in range(1, c):
            for a in range(1, b):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a, b, c, a * b * c


def solve2():

    for b in range(5, 500):
        for a in range(1, b):
            c = 1000 - (a + b)
            if a**2 + b**2 == c**2:
                return a, b, c, a * b * c


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve1)
    print timeit(solve2)
    print timeit(oneliner)
