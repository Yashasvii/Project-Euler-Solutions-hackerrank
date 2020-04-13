"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import math


def smallest_lcm():
    val = 1
    for i in range(1, 21):
        val *= i // math.gcd(i, val)
    return val


if __name__ == '__main__':
    print(smallest_lcm())
