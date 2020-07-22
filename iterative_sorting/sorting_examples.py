def insertion_sort(list_to_sort):
    # Separate the first element from the rest of the array. Think about it as a sorted list of one element.
    # For all other indices, beginning with [1]:
    for i in range(1, len(list_to_sort)):
        # a. Copy the item at that index into a temp variable
        temp = list_to_sort[i]
        # b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        j = i
        while j > 0 and temp < list_to_sort[j - 1]:
            print(j)
            # Shift items over to the right as you iterate
            list_to_sort[j] = list_to_sort[j - 1]
            j -= 1
        # c. When the correct index is found, copy temp into this position
        list_to_sort[j] = temp
    return list_to_sort

my_list = [8, 2, 9.5, 9.7, 27, 5, 4, 5, 1, 3]
print(insertion_sort(my_list))