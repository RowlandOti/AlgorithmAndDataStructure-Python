# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
# Given a 6 by 6 2D array and an hour glass of the shaep of a 3 by 3 array wih only one middle element.
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

sum = []
for i in range(0, 4):
    for j in range(0, 4):
        sum.append(arr[i][j] + arr[i][j+1] + arr[i][j+2]
                             + arr[i+1][j+1] +
                   arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

print(max(sum))