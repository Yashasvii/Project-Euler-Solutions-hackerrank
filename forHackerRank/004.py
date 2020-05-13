"""
Project Euler Problem 4
=======================

"""


# !/bin/python3

# !/bin/python3


def get_palin_set():
    palin_set = set()
    for i in range(100, 1000):
        for j in range(100000 // i + 1, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                palin_set.add(product)

    return palin_set


def print_result():
    palin_set = get_palin_set()
    sorted_palin_list = sorted(palin_set)
    length = len(sorted_palin_list)
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        for i in range(length - 1, -1, -1):
            if sorted_palin_list[i] < n:
                print(sorted_palin_list[i])
                break


if __name__ == '__main__':
    print_result()
