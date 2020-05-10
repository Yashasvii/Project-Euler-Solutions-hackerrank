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


def pytha_calc(N):
    largest = -1
    for a in range(1, N - 4):
        b = (N**2-2*a*N)//(2*N-2*a)
        if b >= 2:
            c = N - a - b
            if a ** 2 + b ** 2 == c ** 2:
                product = a * b * c
                if largest < product:
                    largest = product

    return largest


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(pytha_calc(n))
