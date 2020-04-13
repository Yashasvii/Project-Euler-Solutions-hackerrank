"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pytha_calc():
    for a in range(1, 995 + 1):
        for b in range(a + 1, 996 + 1):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                return a * b * c


if __name__ == '__main__':
    print(pytha_calc())
