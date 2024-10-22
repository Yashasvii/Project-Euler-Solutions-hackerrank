"""
Project Euler Problem 7
=======================

"""
import math


def prime(n, prime_list):
    number = 3
    count = 2

    prime_list_length = len(prime_list)

    if n == 1:
        return 2

    if prime_list_length > 1:
        if prime_list_length >= n:
            return prime_list[n - 1]
        else:
            count = prime_list_length + 1
            number = prime_list[prime_list_length - 1] + 2

    while True:
        is_prime = True
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(number)
            if count == n:
                return number
            else:
                count += 1
        number += 2


if __name__ == '__main__':
    t = int(input().strip())
    prime_list = [2]
    for a0 in range(t):
        num = int(input().strip())
        print(prime(num, prime_list))
