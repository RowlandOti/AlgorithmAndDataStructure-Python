# Colleen is turning N years old! Therefore, she has N candles of various heights on her cake, and candle I has height I.
# Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.
# Given the height I for each individual candle, find and print the number of candles she can successfully blow out.
from collections import Counter


# Method 1
def birthdayCakeBlownCandles(n, arr):
    arr_maxheight_count = (Counter(arr).most_common())[0][1]
    return (arr_maxheight_count)


print("**What is Colleen's Age**")
n = int(input().strip())
print("**Enter the height of the candles**")
arr = [int(x) for x in input().strip().split(' ')]

result = birthdayCakeBlownCandles(n, arr)
print(result)
