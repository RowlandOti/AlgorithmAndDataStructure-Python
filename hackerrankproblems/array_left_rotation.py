# Given an array of  integers and a number, , perform  left rotations on the array.
# Then print the updated array as a single line of space-separated integers.

# Method 1 -Not very efficent
def leftRotation(arr, d):
    arr_size = len(arr)
    for i in range(d):
        for j in range(arr_size - 1):
            swap(arr, j, j + 1)
    return arr

# Method 2
def leftRotation2(arr, d):
    return arr[d:] + arr[0:d]

def swap(arr, first_e, second_e):
    temp = arr[first_e]
    arr[first_e] = arr[second_e]
    arr[second_e] = temp

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))

    print(" ".join(map(str, leftRotation(a, d))))

    print(" ".join(map(str, leftRotation2(a, d))))
