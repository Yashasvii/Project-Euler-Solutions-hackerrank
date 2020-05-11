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
    cases = int(input().strip())
    for i in range(cases):
        N, M = input().strip().split(' ')
        N, M = [int(N), int(M)]
        print(combination((N + M), M) % (
                    10 ** 9 + 7))  # (10**9+7) is added according to hackerran requirement, remove it from euler problem
