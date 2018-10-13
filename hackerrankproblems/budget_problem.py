#!/bin/python3

import sys
import os


# Complete the function below.
def limit_shopping_budget(budget, bundle_costs, bundle_values, bundle_item_count):
    if (budget == 0 or bundle_item_count == 0):
        return 0

    if (bundle_costs[bundle_item_count - 1] > budget):
        return limit_shopping_budget(budget, bundle_costs, bundle_values, bundle_item_count - 1)
    else:
        return max(bundle_values[bundle_item_count - 1] +
                   limit_shopping_budget(budget - bundle_costs[bundle_item_count - 1],bundle_costs, bundle_values, bundle_item_count - 1),
                   limit_shopping_budget(budget, bundle_costs, bundle_values, bundle_item_count - 1))


if (__name__ == "__main__"):
    print("**What is our Budget**")
    budget = int(input())

    print("**What is the no. of Bundles**")
    bundle_item_count = 0
    bundle_item_count = int(input())

    print("**What are the Bundle values**")
    bundle_values = list(map(int, input().strip().split(" ")))

    print("**What are the Bundle costs**")
    bundle_costs = list(map(int, input().strip().split(" ")))

    result = limit_shopping_budget(budget, bundle_costs, bundle_values, bundle_item_count)
    print("Maximum shopping value given constraints is {}".format(result))
