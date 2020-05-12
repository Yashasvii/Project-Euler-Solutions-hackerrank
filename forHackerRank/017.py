"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""


def get_letter(n):
    one_to_nineteen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                       "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                       "Nineteen"]
    others = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return "Zero"

    elif n < 20:
        return one_to_nineteen[n]
    elif n < 100:
        return others[n // 10] + (' ' + one_to_nineteen[n % 10] if n % 10 != 0 else '')
    elif n < 1000:
        return one_to_nineteen[n // 100] + ' ' + 'Hundred' + (
            ' ' + get_letter(n % 100) if n % 100 != 0 else '')
    elif n < 1000000:
        return get_letter(n // 1000) + ' ' + 'Thousand' + (
            ' ' + get_letter(n % 1000) if n % 1000 != 0 else '')
    elif n < 1000000000:
        return get_letter(n // 1000000) + ' ' + 'Million' + (
            ' ' + get_letter(n % 1000000) if n % 1000000 != 0 else '')
    elif n < 1000000000000:
        return get_letter(n // 1000000000) + ' ' + 'Billion' + (
            ' ' + get_letter(n % 1000000000) if n % 1000000000 != 0 else '')
    else:
        return 'One Trillion'


if __name__ == '__main__':
    counts = int(input().strip())
    for i in range(counts):
        num = int(input().strip())
        print(get_letter(num))
