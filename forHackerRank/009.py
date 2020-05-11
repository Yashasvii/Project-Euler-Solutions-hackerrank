"""
Project Euler Problem 9
=======================

"""


def pytha_calc(N):
    largest = -1
    for a in range(1, N - 4):
        b = (N**2-2*a*N)//(2*N-2*a)
        if b >= 2:
            c = N - a - b
            if a ** 2 + b ** 2 == c ** 2:
                product = a * b * c
                if largest < product:
                    largest = product

    return largest


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(pytha_calc(n))
