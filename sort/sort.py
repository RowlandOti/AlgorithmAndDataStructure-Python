class Sorting(object):
    def bubbleSort(self, arr, n):
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if (arr[j] > arr[j + 1]):
                    self.swap(arr, j, j + 1)

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
            pivot  = list[0]
            left_part, right_part = [], []
            for x in list[1:]:
                if (x  <= pivot):
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
        self.swap(arr, end, i+1)
        return i+1

    def swap(self, arr, first, last):
        temp = arr[first]
        arr[first] = arr[last]
        arr[last] = temp


sort = Sorting()

print("********Bubble Sort**********")
arrBubble = [12, 11, 13, 5, 6, 1, 7, 9, 3, 10]
sort.bubbleSort(arrBubble, len(arrBubble))
print(arrBubble)


print("********Selection Sort**********")
arrSelection = [12, 11, 13, 5, 6, 1, 7, 9, 3, 10]
sort.selectionSort(arrSelection, len(arrSelection))
print(arrSelection)

print("********Insertion Sort**********")
arrInsertion = [12, 11, 13, 5, 6, 1, 7, 9, 3, 10]
sort.insertionSort(arrInsertion, len(arrInsertion))
print(arrInsertion)

print("********Quick Sort**********")
arrQuick = [12, 11, 13, 5, 6, 1, 7, 9, 3, 10]
sort.quickSortArray(arrQuick, 0, len(arrQuick) - 1)
print(arrQuick)

print("********Quick Sort**********")
arrQuickList = [12, 11, 13, 5, 6, 1, 7, 9, 3, 10]
arrQuickList = sort.quickSortList(arrQuickList)
print(arrQuickList)
