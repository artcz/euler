# coding: utf-8

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

import time


def oneliner():
    pass


def solve1_naive():
    # pip install num2words
    import num2words

    counter = 0
    for i in range(1, 1000+1):
        counter += len(
            [x for x in num2words.num2words(i) if x.isalpha()]
        )

    return counter


if __name__ == "__main__":

    def timeit(function):
        t1 = time.time()
        output = function()
        t2 = time.time()
        return output, t2-t1

    print timeit(solve1_naive)
    print timeit(oneliner)
