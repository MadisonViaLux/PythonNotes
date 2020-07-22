# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index + 1, len(arr)):
            smallest_index = j
            if arr[smallest_index] < arr[cur_index]:
                # TO-DO: swap
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

print(selection_sort([1, 7, 65, 4987, 55, 69, 87]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    def swap(a, b):
        arr[a], arr[b] = arr[b], arr[a]

    arr_len = len(arr)
    swapped = True
    i = -1
    while swapped:
        swapped = False
        i = i + 1
        for x in range(1, arr_len - i):
            if arr[x - 1] > arr[x]:
                swap(x - 1, x)
                swapped = True
    return arr

print(bubble_sort([1, 7, 65, 4987, 55, 69, 87]))