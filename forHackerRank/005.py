"""
Project Euler Problem 5
=======================

"""
import math


def smallest_lcm(num):
    val = 1
    for i in range(2, num + 1):
        val *= i // math.gcd(i, val)
    return val


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_lcm(n))
