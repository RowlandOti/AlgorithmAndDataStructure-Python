# You are given a list(1-indexed) of size , n initialized with zeroes. You have to perform m operations on the list and output the maximum
# of final values of all the n elements in the list. For every operation, you are given three integers (a, b, k),  and  and you have to add value
#  to all the elements ranging from index a to b (both inclusive).


def elements_replaced(lst, new_element, indices):
    return [new_element if i in indices else e for i, e in enumerate(lst)]


# Method 1 -Slow
if __name__ == "__main__":
    n, m = [int(x) for x in input().strip().split(' ')]

    arr_n = [0] * n
    for num_query in range(m):
        start, end, inc = [int(x) for x in input().strip().split(' ')]
        arr_n[start - 1:end] = [x + inc for x in arr_n[start - 1:end]]
    print(max(arr_n))

# Method 2 -Faster
if __name__ == "__main__":
    list_size, num_queries = [int(x) for x in input().strip().split(' ')]

    arr_n = [0] * list_size
    for query in range(num_queries):
        start, end, inc = [int(x) for x in input().strip().split(' ')]
        arr_n[start - 1] += inc
        try:
            arr_n[end] -= inc
        except:
            # out of range of list (at the end)
            pass

    prev = 0
    for query in range(len(arr_n)):
        prev += arr_n[query]
        arr_n[query] = prev

    print(max(arr_n))
