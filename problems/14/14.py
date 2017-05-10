# coding: utf-8

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time


def oneliner():
    """TODO: write oneliner"""
    pass


def solve1():

    def next(n):
        if n % 2 == 0:
            return n // 2
        return 3*n + 1

    sequences_lengths = {}

    for i in range(2, 10**6):
        if i % 10**5 == 0:
            print i

        sequence = [i]
        j = i
        while j != 1:
            j = next(j)
            sequence.append(j)

        sequences_lengths[i] = len(sequence)

    return max(sequences_lengths.iteritems(), key=lambda x: x[1])


def solve2():

    def collatz(n):
        length = 0

        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3*n + 1

            length += 1

        return length + 1  # final one.

    longest = 0
    for i in range(2, 10**6):
        if i % 10**5 == 0:
            print i

        length = collatz(i)
        if length > longest:
            longest = length

    return longest


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve1)
    print timeit(solve2)
    # print timeit(oneliner)
