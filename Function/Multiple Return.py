"""
Multiple return in python
"""


def count(lst):
    even = 0
    odd = 0
    for item in lst:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


lst = [10, 3, 33, 24, 45, 23, 54, 65, 22]

total_even, total_odd = count(lst)
print(f"Total number of even = {total_even}")
print(f"Total number of odd = {total_odd}")