"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
import math


def prime():
    number = 2
    count = 1
    while True:
        is_prime = all(number % i != 0 for i in range(2, int(math.sqrt(number) + 1)))
        if is_prime:
            if count == 10001:
                return number
            else:
                count += 1
        number +=1


if __name__ == '__main__':
    print(prime())
