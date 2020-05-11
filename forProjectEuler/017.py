"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""


def total_letter_count():
    one_to_nineteen = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    others = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
    for letter in range(1, 1001):
        total_sum = sum(each_letter_count(i, one_to_nineteen, others) for i in range(1, 1001))
        return total_sum


def each_letter_count(n, one_to_nineteen, others):
    if n < 20:
        return one_to_nineteen[n]
    elif n < 100:
        return others[n // 10] + one_to_nineteen[n % 10]
    elif n < 1000:
        return one_to_nineteen[n // 100] + 7 + 3 + each_letter_count(n % 100, one_to_nineteen,
                                                                     others) if n % 100 != 0 else one_to_nineteen[
                                                                                                      n // 100] + 7
    else:
        return 11  # One Thousand


if __name__ == '__main__':
    print(total_letter_count())
