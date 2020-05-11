"""
Project Euler Problem 10
========================

"""
import math


def sum_prime(num_below, list_sum):
    sum_num = 0
    start = 2
    length = len(list_sum)
    if length > 2:
        if length-1 >= num_below:
            return list_sum[num_below]
        else:
            start = length
            sum_num = list_sum[length - 1]

    for num in range(start, num_below + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            sum_num += num
        list_sum.append(sum_num)

    return sum_num


if __name__ == '__main__':
    t = int(input().strip())
    list_prime_sum = [0, 0]
    for a0 in range(t):
        n = int(input().strip())
        print(sum_prime(n, list_prime_sum))
