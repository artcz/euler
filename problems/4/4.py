# coding: utf-8

"""
To run:
    python2.7 4.py

Problem:
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time


def oneliner():
    """
    three_digit_numbers = range(100, 1000)
    products = [
        x*y
        for x in three_digit_numbers
        for y in three_digit_numbers
    ]
    is_palindrome = lambda x: str(x) == str(x)[::-1]
    return max(p for p in products if is_palindrome(p))
    """

    return max(
        p for p
        in [x*y for x in range(100, 1000) for y in range(100, 1000)]
        if str(p) == str(p)[::-1]
    )


def solve1():

    def is_palindrome(n):
        str_from_int = str(n)
        return str_from_int == str_from_int[::-1]

    three_digit_numbers = range(100, 1000)
    products_of_three_digit_numbers = [
        x*y for x in three_digit_numbers
            for y in three_digit_numbers
    ]

    palindromes = [
        p for p in products_of_three_digit_numbers
          if is_palindrome(p)
    ]

    return max(palindromes)


def solve2():

    def is_palindrome(n):
        original = n
        reversed = 0
        while n > 0:
            reversed = reversed * 10 + n % 10
            n //= 10

        return original == reversed

    i, _max, largest_palindrome = 100, 1000, 0

    while i < _max:
        j = 100
        while j < _max:
            product = i*j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
            j += 1
        i += 1

    return largest_palindrome

def solve3():

    def is_palindrome(n):
        original = n
        reversed = 0
        while n > 0:
            reversed = reversed * 10 + n % 10
            n //= 10

        return original == reversed

    three_digit_numbers = range(100, 1000)
    products_of_three_digit_numbers = [
        x*y for x in three_digit_numbers
            for y in three_digit_numbers
    ]

    palindromes = [
        p for p in products_of_three_digit_numbers
          if is_palindrome(p)
    ]

    return max(palindromes)


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve1)
    print timeit(solve2)
    print timeit(solve3)
    print timeit(oneliner)
