#!/usr/bin/python

# find the number of ways to reach a total with the given number of combinations

change = 200
denominations = [25, 10, 5, 1]
names = {25: "quarter(s)", 10: "dime(s)", 5: "nickel(s)", 1: "pennies"}


# Method 1
def cntComb(change_amount_left, coins_available, coin_start_index=0):
    if (change_amount_left == 0): return 1
    elif (change_amount_left < 0 or len(coins_available) == coin_start_index):
        return 0
    else:
        with_ith_coin_solution = cntComb(change_amount_left - coins_available[coin_start_index], coins_available, coin_start_index)
        without_ith_coin_solution = cntComb(change_amount_left, coins_available, coin_start_index + 1)
    return with_ith_coin_solution + without_ith_coin_solution

# Method 2
def cntComb2(change_amount_left, coins_available, coin_start_index, comb_list, comb):
    if (comb):
        comb_list.append(comb)
    if (change_amount_left == 0 or len(coins_available) == coin_start_index + 1):
        if (coin_start_index + 1) == len(coins_available) and change_amount_left > 0:
            comb_list.append((change_amount_left, coins_available[coin_start_index]))
            coin_start_index += 1
        while coin_start_index < len(coins_available):
            comb_list.append((0, coins_available[coin_start_index]))
            coin_start_index += 1
        print(" ".join("%d %s" % (n, names[c]) for (n, c) in comb_list))
        return 1
    cur = coins_available[coin_start_index]
    return sum(
        cntComb2(change_amount_left - x * cur, coins_available, coin_start_index + 1, comb_list[:], (x, cur)) for x
        in range(0, int(change_amount_left / cur) + 1))


print(cntComb(change, denominations))
print(cntComb2(change, denominations, 0, [], None))
