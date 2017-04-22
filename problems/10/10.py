# coding: utf-8

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


import math
import time


def oneliner():

    return sum(
        p
        for p in range(2, int(2e6))
        if (all(p % j != 0
                for j in range(2, int(math.sqrt(p)) + 1))
            and p >= 2)
    )


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


def solve3():
    """Eratosthenes"""
    total = int(2e6)
    numbers = [[i, True] for i in range(total + 1)]
    for t in range(2, int(math.sqrt(total)) + 1):
        if numbers[t][1]:
            for m in range(2*t, total + 1, t):
                numbers[m][1] = False


    return sum(x for x, y in numbers if y and x >= 2)


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve3)
    print timeit(solve2)
    print timeit(solve1)
    print timeit(oneliner)
