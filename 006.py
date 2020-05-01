"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
import math


def sum_of_natural_number(n):
    return (n * (n + 1) // 2) ** 2


def sum_of_squares_of_natural_number(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


def final_ans(n):
    return sum_of_natural_number(n) - sum_of_squares_of_natural_number(n)


t = int(input().strip())
for a0 in range(t):
    num = int(input().strip())
    print(final_ans(num))
