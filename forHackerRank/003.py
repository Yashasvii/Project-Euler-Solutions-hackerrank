import math

"""
Project Euler Problem 3
=======================

"""


def largest_prime(num):
    while True:
        small_prime_fac = smallest_prime_factor(num)
        if small_prime_fac < num:
            num //= small_prime_fac
        else:
            return num


def smallest_prime_factor(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return i
    return num


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime(n))
