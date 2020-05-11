"""
Project Euler Problem 6
=======================

"""


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
