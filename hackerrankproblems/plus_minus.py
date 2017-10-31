#!/bin/python3

# Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which
# fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.
#
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10-4 are acceptable.

class PlusMinus(object):
    arr = []

    def __init__(self):
        self.take_input()

    def take_input(self):
        print("**What is the size of the Array**")
        n = int(input().strip())
        print("**Enter Array items seperated by space**")
        self.arr = [int(x) for x in input().strip().split(' ')]
        print("**Array as Entered**")
        print(*self.arr)

    def calculate_ratios(self):
        print(format(len([x for x in self.arr if x > 0]) / len(self.arr), ".6f"))
        print(format(len([x for x in self.arr if x < 0]) / len(self.arr), ".6f"))
        print(format(len([x for x in self.arr if x == 0]) / len(self.arr), ".6f"))


plus_minus = PlusMinus()

plus_minus.calculate_ratios()
