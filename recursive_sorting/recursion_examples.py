def recurse(number):
    if number == 0:
        return
    print(number)
    number -= 1
    recurse(number)


recurse(10)



def recurse(n):
    if n > 0:
        print(n)
        recurse(n-1)


recurse(5)



def recurse(number):
    if number <= 0:
        return
    print(number)
    number -= 1
    recurse(number)


recurse(3)



def fibonacci(n):
    if n < 0:
        print("Negative numbers are not valid")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Return (n - 1) + (n - 2)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(16)) # Maxes at 39



my_list = [5, 9, 3, 7, 2, 8, 1, 6]
def partition(data):
    left = []
    pivot = data[0]
    right = []
    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else:  # Handling > or =
            right.append(item)
    return left, pivot, right

def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort(my_list))