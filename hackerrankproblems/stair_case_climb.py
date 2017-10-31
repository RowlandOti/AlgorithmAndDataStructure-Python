#!/bin/python3

# You are climbing a stair case. Each time you can either make 1 step or 2 steps.
# The staircase has n steps. In how many distinct ways can you climb the staircase?

# Recurssive program to find n'th fibonacci number
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# returns no. of ways to reach s'th stair
def countWays(s):
    return fib(s + 1)


# Driver program

s = int(input().strip())
print("Number of ways = ",)
print(countWays(s))
