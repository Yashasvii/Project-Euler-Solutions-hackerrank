import math

"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
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


if __name__ == '__main__':
    print(largest_prime(600851475143))
