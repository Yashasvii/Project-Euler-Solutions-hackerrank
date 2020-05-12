"""
Project Euler Problem 12
========================

The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
28. The first ten terms would be:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

   1: 1
   3: 1,3
   6: 1,2,3,6
  10: 1,2,5,10
  15: 1,3,5,15
  21: 1,3,7,21
  28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""
import math


def triangular_number(N, factor_count_list):
    i = 1
    length = len(factor_count_list)
    while True:
        if length > i:
            count_factor = factor_count_list[i]
        else:
            prime_factor_count = {}
            if i % 2 == 0:
                find_factors(i // 2, prime_factor_count)
                find_factors(i + 1, prime_factor_count)
            else:
                find_factors((i + 1) // 2, prime_factor_count)
                find_factors(i, prime_factor_count)

            count_factor = 1
            for j in prime_factor_count.values():
                count_factor *= (
                        j + 1)  # if the prime factors of a number is a^n , b^m , c^q then the number of divisors is (n+1)(m+1)(q+1)
            factor_count_list.append(count_factor)
        if count_factor > N:
            return i * (i + 1) // 2
        i += 1


#
# def find_factors(num):
#     square_root = math.sqrt(num)
#     count_factor = 0
#     for i in range(2, int(square_root + 1)):
#         if num % i == 0:
#             count_factor = count_factor + 1
#     count_factor = 2 * count_factor + 1 if square_root ** 2 == num else 2 * count_factor + 2
#     return count_factor


def find_factors(num, prime_factor_count):
    while num % 2 == 0:
        if 2 in prime_factor_count:
            prime_factor_count[2] += 1
        else:
            prime_factor_count[2] = 1
        num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            if i in prime_factor_count:
                prime_factor_count[i] += 1
            else:
                prime_factor_count[i] = 1
            num //= i
    if num > 2:
        if num in prime_factor_count:
            prime_factor_count[num] += 1
        else:
            prime_factor_count[num] = 1


if __name__ == '__main__':

    count_factor_list = [None]
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(triangular_number(n, count_factor_list))