def optimus(max_sum, a_list, start_index):
    if (max_sum == 0 or start_index == 0):
        return 0
    elif (a_list[start_index - 1] > max_sum):
        return optimus(max_sum, a_list, start_index - 1)
    else:
        with_ith_a = a_list[start_index - 1] + optimus(max_sum - a_list[start_index - 1], a_list, start_index)
        without_ith_a = optimus(max_sum, a_list, start_index - 1)
        return max(with_ith_a, without_ith_a)


def knapsack(max_sum, a_list, n):
    dp = [0] * (max_sum+1)
    for i in range(1, n+1):
        for j in range(1, max_sum+1):
            if j >= a_list[i-1]:
                dp[j] = max(dp[j], dp[j-a_list[i-1]]+a_list[i-1])
    return dp[-1]

T_CASES = int(input().strip())

for i in range(T_CASES):
    A_LEN, K_SUM = [int(x) for x in input().strip().split(" ")]
    A_LIST = [int(x) for x in input().strip().split(" ")]
    print(optimus(K_SUM, A_LIST, A_LEN -1))
    print(knapsack(K_SUM, A_LIST, A_LEN))