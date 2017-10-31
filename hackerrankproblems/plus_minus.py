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
        print("********What is the size of the Array**********")
        n = int(input().strip())
        print("********Enter Array items seperated by space**********")
        self.arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        print("**Array as Entered**")
        print(*self.arr)

    def calculate_ratios(self):
        pos_count, neg_count, zero_count = 0, 0, 0
        pos_zero_neg = []
        for number in self.arr:
            if(number > 0):
                pos_count += 1
            elif (number < 0):
                neg_count += 1
            else:
                zero_count += 1
        print(pos_count/len(self.arr))
        print(neg_count / len(self.arr))
        print(zero_count / len(self.arr))


plus_minus = PlusMinus()

plus_minus.calculate_ratios()