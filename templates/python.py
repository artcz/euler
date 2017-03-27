# coding: utf-8

"""
To run:
    python2.7 <foo>.py

Problem:
    <description>
"""

import time


def oneliner():
    return []


def impl1():
    return []


def impl2():
    return []


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(impl1)
    print timeit(impl2)
    print timeit(oneliner)
