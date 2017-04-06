# coding: utf-8

"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import time


def oneliner():
    return abs(sum([x**2 for x in range(100+1)]) - sum(range(100+1))**2)


def solve1():
    def sum_of_squares(n):
        squares = []
        for i in range(n+1):
            squares.append(i**2)
        return sum(squares)

    def square_of_sum(n):
        return sum(range(n+1))**2

    return abs(sum_of_squares(100) - square_of_sum(100))


def solve2():
    _sum, _sum_of_squares, N = 0, 0, 100

    for i in range(N+1):
        _sum += i
        _sum_of_squares += i**2

    return abs(_sum**2 - _sum_of_squares)


if __name__ == "__main__":
    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve1)
    print timeit(solve2)
    print timeit(oneliner)
