"""
Project Euler Problem 2
=======================

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
