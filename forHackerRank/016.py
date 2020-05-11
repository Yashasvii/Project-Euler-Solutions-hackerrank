"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def sum_of_digit(n):
    num = 2 ** n
    result = sum(int(i) for i in str(num))
    return result


if __name__ == '__main__':
    count = int(input().strip())
    for i in range(count):
        power = int(input().strip())
        print(sum_of_digit(power))
