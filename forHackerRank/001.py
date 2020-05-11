"""
Project Euler Problem 1
=======================
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
