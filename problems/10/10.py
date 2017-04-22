# coding: utf-8

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import math
import time


def oneliner():
    "TODO: write oneliner"
    pass


def solve1():
    primes = []

    counter = 2
    while True:
        for i in range(2, int(math.sqrt(counter))+1):
            if counter % i == 0:
                break
        else:
            primes.append(counter)

        counter += 1
        if counter > 2*10**6:
            break

    return sum(primes)


def solve2():

    _sum = 0
    for i in range(2, int(2e6)):
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            _sum += i

    return _sum



if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    # print timeit(solve1)
    print timeit(solve2)
    print timeit(oneliner)
