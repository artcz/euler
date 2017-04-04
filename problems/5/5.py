#!/usr/bin/env python2.7
# coding: utf-8

"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import itertools
import time


def oneliner():
    """
    Runnig this one on i5 4690
    python p5.py  298.32s user 3.45s system 65% cpu 7:37.40 total
    [plus system freeze, and stuff...]
    """
    return [
        z for z in
        itertools.takewhile(
            lambda x: not all([x % j == 0 for j in range(2, 20)]),
            itertools.count(1)
        )
    ][-1]+1


def solve():
    """
    Running on i5 4690:
        python p5.py  81.91s user 0.03s system 100% cpu 1:21.86 total
    """
    i = 2520
    while True:
        for j in range(2, 21):
            if i % j != 0:
                break
        else:
            return i

        if i % 1e6 == 0:
            print i
        i += 1


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    # On pypy:
    # (232792560, 10.906013011932373)
    # (232792560, 102.8434100151062)
    print timeit(solve)
    print timeit(oneliner)
