#!/bin/python3

# Recursive and iterative Fibonacci series
import math

import time


def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_goldenratio_faster(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    val = (golden_ratio ** n - (1 - golden_ratio) ** n) / math.sqrt(5)
    return int(round(val))


print("**Fibonnacci series for which No.?**")
N = int(input().strip())

start_time = time.time()
print([fib_recursive(i) for i in range(N)])
print("time elapsed - recursive: {:.6f}s".format(time.time() - start_time))

start_time = time.time()
print([fib_iterative(i) for i in range(N)])
print("time elapsed - iterative: {:.6f}s".format(time.time() - start_time))

start_time = time.time()
print([fib_goldenratio_faster(i) for i in range(N)])
print("time elapsed - formulae: {:.6f}s".format(time.time() - start_time))
