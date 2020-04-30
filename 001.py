"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_natural_num(n, div):
    n = (n - 1) // div
    return n * (n + 1) // 2


def find_sum(n):
    return 3 * sum_of_natural_num(n, 3) + 5 * sum_of_natural_num(n, 5) - 15 * sum_of_natural_num(n, 15)


if __name__ == '__main__':
    # !/bin/python3
    t = int(input().strip())
    three_or_five_dict = {}
    for a0 in range(t):
        num = int(input().strip())
        print(find_sum(num))
