import datetime
import numpy as np

class Sorting(object):
    def bubbleSort(self, arr, n):
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if (arr[j] > arr[j + 1]):
                    self.swap(arr, j, j + 1)

    def mergeSort(self, arr, n):
        if (n < 2):
            return
        mid = n // 2
        arr_one = arr[:mid]
        arr_two = arr[mid:]

        self.mergeSort(arr_one, len(arr_one))
        self.mergeSort(arr_two, len(arr_two))
        self.merge(arr, arr_one, arr_two)

    def merge(self, arr, arr_one, arr_two):
        i, j, k = 0, 0, 0
        while (i < len(arr_one) and j < len(arr_two)):
            if (arr_one[i] < arr_two[j]):
                arr[k] = arr_one[i]
                i += 1
            else:
                arr[k] = arr_two[j]
                j += 1
            k += 1
        while (i < len(arr_one)):
            arr[k] = arr_one[i]
            i += 1
            k += 1
        while (j < len(arr_two)):
            arr[k] = arr_two[j]
            j += 1
            k += 1

    def selectionSort(self, arr, n):
        for i in range(n):
            # Assume min is the first element
            min = i
            # Check if there is other lower than current min
            for j in range(i + 1, n - 1):
                if (arr[min] > arr[j]):
                    # update min
                    min = j
            self.swap(arr, min, i)

    def insertionSort(self, arr, n):
        # Traverse through 1 to len(arr)
        for i in range(0, n):
            cursor = arr[i]
            # move elements of arr[0....i-1] (left-side), that are greater than cursor, to one position ahead of their current position
            cursor_pointer = i
            while (cursor_pointer > 0 and cursor < arr[cursor_pointer - 1]):
                arr[cursor_pointer] = arr[cursor_pointer - 1]
                cursor_pointer -= 1
            # move current cursor to its correct position
            arr[cursor_pointer] = cursor

    def quickSortList(self, list):
        if (len(list) <= 1):
            return list
        else:
            pivot = list[0]
            left_part, right_part = [], []
            for x in list[1:]:
                if (x <= pivot):
                    left_part.append(x)
                else:
                    right_part.append(x)
            return self.quickSortList(left_part) + [pivot] + self.quickSortList(right_part)

    def quickSortArray(self, arr, start, end):
        if (start >= end):
            return
        pivot_pointer = self.partitionCollection(arr, start, end)
        # sort the left side
        self.quickSortArray(arr, start, pivot_pointer - 1)
        # sor the right side
        self.quickSortArray(arr, pivot_pointer + 1, end)

    def partitionCollection(self, arr, start, end):
        pivot = arr[end]
        # index of the smaller element
        i = start - 1
        for j in range(start, end):
            if (arr[j] <= pivot):
                # increment index of smaller element
                i += 1
                # move element < pivot to the left
                self.swap(arr, j, i)
        # move pivot to correct position
        self.swap(arr, end, i + 1)
        return i + 1

    def swap(self, arr, first, last):
        temp = arr[first]
        arr[first] = arr[last]
        arr[last] = temp

    def time_print(self, fun, time_info):
        print('{} execution took {} seconds.'.format(fun.__name__, time_info))


sort = Sorting()
# arrRandom = [random.choice([i for i in range(100000)]) for r in range(100)]
arrRandom = np.random.randint(0, 1000, 100)

print("********Bubble Sort**********")
arrBubble = list(arrRandom)
now = datetime.datetime.now()
sort.bubbleSort(arrBubble, len(arrBubble))
print(arrBubble)
sort.time_print(sort.bubbleSort, datetime.datetime.now() - now)

print("********Merge Sort**********")
arrMerge = list(arrRandom)
now = datetime.datetime.now()
sort.mergeSort(arrMerge, len(arrMerge))
print(arrMerge)
sort.time_print(sort.mergeSort, datetime.datetime.now() - now)

print("********Selection Sort**********")
arrSelection = list(arrRandom)
now = datetime.datetime.now()
sort.selectionSort(arrSelection, len(arrSelection))
print(arrSelection)
sort.time_print(sort.selectionSort, datetime.datetime.now() - now)

print("********Insertion Sort**********")
arrInsertion = list(arrRandom)
now = datetime.datetime.now()
sort.insertionSort(arrInsertion, len(arrInsertion))
print(arrInsertion)
sort.time_print(sort.insertionSort, datetime.datetime.now() - now)

print("********Quick Sort**********")
arrQuick = list(arrRandom)
now = datetime.datetime.now()
sort.quickSortArray(arrQuick, 0, len(arrQuick) - 1)
print(arrQuick)
sort.time_print(sort.quickSortArray, datetime.datetime.now() - now)

print("********Quick Sort**********")
arrQuickList = list(arrRandom)
now = datetime.datetime.now()
arrQuickList = sort.quickSortList(arrQuickList)
print(arrQuickList)
sort.time_print(sort.quickSortList, datetime.datetime.now() - now)
