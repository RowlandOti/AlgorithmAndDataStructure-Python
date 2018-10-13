#!/bin/python3

# Consider a staircase of size N =4.

# Observe that its base and height are both equal to N, and the image is drawn using `#`
# symbols and spaces. The last line is not preceded by any spaces. Write a program that prints a staircase of size N.

print("**What is the size of the Staircase**")
N = int(input().strip())

# Method 1
for i in range(1,N+1):
    print(' ' * (N - i) + '#' * i)

# Method 2
[print(' ' * (N - i) + '#' * i) for i in range(1, N + 1)]
