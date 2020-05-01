"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
import math

def smallest_lcm(n):
    val = 1
    for i in range(2, n+1):
        val *= i // math.gcd(i, val)
    return val


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_lcm(n))
