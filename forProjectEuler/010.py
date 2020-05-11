"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math


def sum_prime(num_below):
    sum = 0
    for num in range(2, num_below):
        is_prime = all(num % i != 0 for i in range(2, int(math.sqrt(num) + 1)))
        if (is_prime):
            sum += num
    return sum


if __name__ == '__main__':
    print(sum_prime(2000000))
