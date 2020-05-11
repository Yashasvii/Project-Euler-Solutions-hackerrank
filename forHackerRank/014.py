"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def get_count(N, count_list, beloworequal_n_highest_count, beloworequal_n_highest_number):
    length = len(beloworequal_n_highest_count)

    if length >= N:
        return beloworequal_n_highest_number[N - 1]
    else:
        starting_range = length + 1
        highest_count = beloworequal_n_highest_count[length - 1]
        reqd_num = beloworequal_n_highest_number[length - 1]
    for starting_num in range(starting_range, N + 1):
        num = starting_num
        cou = 1
        while num != 1:
            if num <= len(count_list):
                cou += count_list[num - 1] - 1
                break
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
            cou += 1
        count_list.append(cou)
        highest_count_temp = highest_count
        if highest_count <= cou:
            reqd_num = starting_num
            highest_count = cou
            beloworequal_n_highest_count.append(highest_count)
            beloworequal_n_highest_number.append(starting_num)
        else:
            beloworequal_n_highest_count.append(highest_count_temp)
            beloworequal_n_highest_number.append(reqd_num)

    return reqd_num


if __name__ == '__main__':
    count = int(input().strip())
    st_count_list = [1]
    beloworequal_n_highest = [1]
    beloworequal_n_highest_num = [1]

    for i in range(count):
        n = int(input().strip())
        print(get_count(n, st_count_list, beloworequal_n_highest, beloworequal_n_highest_num))
