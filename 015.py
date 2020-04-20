"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""
import math


def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if __name__ == "__main__":
    num = 5
    print(combination(num * 2, num))
