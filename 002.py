"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""


def fibonacci_sum(n):
    i = 1
    j = 2
    sum = 0
    while i < n:
        temp = i
        if i % 2 == 0:
            sum += i
        i = j
        j = j + temp
    return sum


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(fibonacci_sum(n))
