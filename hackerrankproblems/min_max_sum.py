# Given five positive integers, find the minimum and maximum values that can be
# calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
from functools import reduce

print("**Provide the five integers**")
arr = sorted([int(x) for x in input().strip().split(' ')])

min_sum = reduce(lambda x, y: (x + y), arr[:4])
print(min_sum ,end=' ')
max_sum = reduce(lambda x, y: (x + y), arr[-4:])
print(max_sum)
