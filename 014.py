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


def get_count():
    st_count_dict = {}
    max_num = 0
    max_starting_num =None
    for starting_num in range(1, 1000000):
        num = starting_num
        count = 1
        while num != 1:
            if num in st_count_dict:
                count += st_count_dict[num]
                break
            if num % 2 == 0:
                num /= 2
            else:
                num = 3 * num + 1
            count += 1
        st_count_dict[starting_num] = count
        if max_num < count:
            max_num = count
            max_starting_num = starting_num
    return max_starting_num


if __name__ == '__main__':
    print(get_count())
