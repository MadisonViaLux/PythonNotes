##############################################################################################################

# Equalize Array
# def equalizeArray(arr):
#     x = 2 #<--------------------from 0 to 2
#     extraArr = []
#
#     for i in arr:
#         # 1
#         AC = arr.count(i)
#         # 2
#         if AC >= x:
#             x = AC
#         elif AC < x:
#             extraArr.append(i)
#     # 3
#     le = len(extraArr)
#     print(le)
#     return le
#
# equalizeArray([1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 8, 8, 8])
# equalizeArray([1, 2, 2, 4])
# #1 we want to loop through the array and count how many there are of each item in the array.
# #2 then store the largest number of that count to x, and if it's smaller we append that to another list.
# #3 this allows us to count the appended list as our intended result beacuse it's adding to it everything that's not the highest even number.

# def equalizeArrayNon(data):
#
#     extraArr =[]
#
#     for i in data:
#         if data.count(i) == 1:
#             extraArr.append(i)
#     lenArr = len(extraArr)
#     print(lenArr)
#     return lenArr
#
# equalizeArrayNon([1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 8, 8, 8])








# Filtering Signals
# def countSignals(frequencies, filterRanges):
#
#     # print(filterRanges)
#     # print(frequencies)
#     # Freq = frequencies
#     finalNums = []
#     spareNums = []
#     trashNums = []
#     # print("\nGood: ", finalNums)
#     # print("Spare: ", spareNums)
#     # print("Trash: ", trashNums)
#
#     def filterOne():
#         for FR1 in filterRanges:
#             # print(FR1)
#             for FQ in frequencies:
#                 # print(FQ)
#                 if FR1[0] <= FQ <= FR1[1]:
#                     spareNums.append(FQ)
#                     frequencies.remove(FQ)
#                 else:
#                     trashNums.append(FQ)
#                     frequencies.remove(FQ)
#
#     filterOne()
#     # print("\nFinal: ", finalNums)
#     # print("Spare: ", spareNums)
#     # print("Trash: ", trashNums)
#
#     def filterTwo():
#         newA = list(set(spareNums))
#         newB = list(set(trashNums))
#         # print("\n", newA, newB)
#
#         for A in newA:
#             # print(A)
#             for B in newB:
#                 # print(B)
#                 if A == B:
#                     newA.remove(A)
#
#         finalNums.append(len(set(newA)))
#
#         # print("\n****HERE*****", newA)
#         # print("\n****HERE*****", finalNums)
#         # return finalNums
#
#     filterTwo()
#
#
#     print("\nFinal: ", finalNums)
#     # print("Spare: ", spareNums)
#     # print("Trash: ", trashNums)
#     return finalNums
#
# countSignals([7, 1, 15, 56, 13, 15, 14], [[11,17], [13, 14], [14, 17] ])









# Frequency Queries









# Adding Lowest Numbers
# def addingLowestNumbers(data):
#
#     newList = []
#
#     for i in data:
#         x = i[0]
#
#         if len(i) == 1:
#             newList.append(x)
#         else:
#             for j in i:
#                 if j < x:
#                     x = j
#             newList.append(x)
#
#     # print(newList)
#     print(sum(newList))
#     return sum(newList)
#
#
# addingLowestNumbers([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]])









# Balanced Brackets
# def balancedBrackets(string):
#     # Create a stack
#     stack = []
#     # Create place to store number of pipes
#     pipes = 0
#     # Store all the brackets in a dict
#     brackets = {'[': ']', '{': "}", '(': ')', '|': '|'}
#
#     # First we want to loop through each letter in the string for an opening bracket
#     for x in string:
#
#         # When we find an opening bracket
#         if x in brackets:
#
#             # We want to check to see if it's a pipe
#             if x == '|':
#                 # Increment the number of pipes
#                 pipes += 1
#                 # Then if the number of pipes is even and the top of stack is a pipe
#                 if pipes % 2 == 0 and brackets[stack[-1]] == x:
#                     # Delete or pop off the stack and continue
#                     stack.pop()
#                     continue
#
#             # Append the bracket to stack
#             stack.append(x)
#             continue
#
#         # To move through the string if not a bracket, skip over and continue without breaking loop
#         if x not in brackets.values():
#             continue
#
#         # If the top of stack's opening string is the corresponding closing string, remove or pop off stack
#         if brackets[stack[-1]] == x:
#             stack.pop()
#         else:
#             return 0
#
#     # Returning statement if equal, "True/Fale"
#     return len(stack) == 0









# Making Anagrams
# def makeAnagrams(a, b):
#
#     poppedLetters = []
#     valA = sorted(a)
#     valB = sorted(b)
#     toBeReturned = 0
#     x = 0
#
#     if len(a) > len(b):
#         smallArr = valB
#         biggerArr = valA
#     elif len(a) == len(b):
#         smallArr = valB
#         biggerArr = valA
#     else:
#         smallArr = valA
#         biggerArr = valB
#
#     if (valA == valB):
#         toBeReturned = len(poppedLetters)
#     else:
#         while (valA != valB):
#             # print("\nbiggerArr", biggerArr)
#             # print("smallArr", smallArr)
#             # print(f"Comparing *{biggerArr[x]}* from biggerB to *{smallArr[x]}* from smallA")
#             # print("Letter removed list", poppedLetters)
#             if smallArr[x] != biggerArr[x]:
#                 if biggerArr[x] not in smallArr[x:]:
#                     poppedLetters.append(biggerArr[x])
#                     biggerArr.remove(biggerArr[x])
#                 elif biggerArr[x] in smallArr[x:]:
#                     poppedLetters.append(smallArr[x])
#                     smallArr.remove(smallArr[x])
#                 elif not smallArr[x]:
#                     poppedLetters.append(biggerArr[x:])
#                     biggerArr.remove(biggerArr[x:])
#             else:
#                 x += 1
#
#         toBeReturned = len(poppedLetters)
#
#     print(toBeReturned)
#     return toBeReturned
#
# makeAnagrams("kjdyuerdrghhentgbs", "kytrjtfrsefgibe")
# makeAnagrams("cde", "abc")









# Selection Sort
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         # smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         for j in range(cur_index + 1, len(arr)):
#             smallest_index = j
#             if arr[smallest_index] < arr[cur_index]:
#                 arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
#
#         # TO-DO: swap
#     print(arr)
#     return arr
#
# selection_sort([1, 7, 65, 4987, 55, 69, 87])









# Partition Array
# def partitionArray(k, numbers):
#     x = 1
#     # print("step 1")
#     for i in numbers:
#         # print("step 2")
#         if len(numbers[:x]) == k:
#             # print("step 3")
#             newArr = numbers[x:]
#             currentArr = numbers[:x]
#
#             if len(currentArr) != len(set(currentArr)):
#                 # print("step 4")
#                 return print("No")
#             elif k >= len(newArr):
#                 # print("step 5")
#                 endArr = numbers[-k:]
#                 if len(endArr) != len(set(endArr)):
#                     # print("step 6")
#                     return print("No")
#                 else:
#                     # print("step 7")
#                     return print("Yes")
#
#             elif len(currentArr) == len(set(currentArr)):
#                 # print("step 8")
#                 partitionArray(k, newArr)
#                 return
#         else:
#             x += 1
#
# partitionArray(3, [1, 3, 2, 4, 6, 5, 7, 8])









# Remove Kth Linked List Node
# def removeKthLinkedListNode(head, k):
#     # Setting the length and setting current_node to head
#     length = 0
#     current_node = head
#     # Obtaining the length of the LL by iterating through it
#     while current_node:
#         current_node = current_node.next
#         length += 1
#
#     # If k is > than length, return head
#     if k > length:
#         return head
#
#     # If k is = to length then the head must be removed, then we'll return the next node after head
#     if k == length:
#         return head.next
#
#     # Subtracting the length by k to get the location of the desired node and resetting the current_node to head
#     index_k = length - k
#     counter = 0
#     current_node = head
#
#     # Iterating through the LL one more time to remove the node at position length - k
#     while current_node:
#         # Checking if the counter is right before the k node
#         if counter == index_k - 1:
#             # Grabbing the node *after k
#             next_k_node = current_node.next.next
#             # Then setting current_node to next_k_node, basically jumping chain and removing desired node
#             current_node.next = next_k_node
#             # Break the loop because node was deleted
#             break
#         # Moving the node forward and incrementing the counter
#         current_node = current_node.next
#         counter += 1
#
#     return head









# Three Number Sum
# def threeNumberSum(arr, target):
#     # Create a hashtable to store the third number as a key to the values of the other two numbers ([3:1,2])
#     hashtable = {}
#     # Create a list to return the values after converted without dupes
#     sum_list = set()
#
#     # Double loop through the arr to compare all numbers
#     for i in arr:
#         for j in arr:
#
#             # Pass over if same num
#             if i == j:
#                 continue
#
#             # To get the third_num, we'll add both i and j and subtract it from the *target
#             third_num = target - (i + j)
#             # Then store them in the hashtable as the key:value pair ([3:1,2])
#             hashtable[third_num] = [i, j]
#             # print(hashtable)
#
#     # Looping a second time
#     for i in arr:
#
#         # Check if the nums from the arr, [i as key], are in the hashtable [key]
#         if i in hashtable:
#
#             # Then check to see that arr[i] isn't in the hashtable arr value, each number must be distinct
#             if i not in hashtable[i]:
#                 # Setting new_list to the values of the 3rd number ([#:1,2])
#                 new_list = hashtable[i]
#                 # Taking the key, 3rd number, and appending it to new_list ([1,2,3])
#                 new_list.append(i)
#                 # Sorting new_list so it's in order
#                 new_list = sorted(new_list)
#                 # Adding new_list as a Tuple into sum_list to remove dupes
#                 sum_list.add(tuple(new_list))
#
#     # Converting the Tuples back into list format
#     sum_list = [list(tup) for tup in sum_list]
#
#     return sorted(sum_list)
#
#
# print(threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0)) #<---------- [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-5, -1, 6], [-5, 0, 5], [-5, 2, 3], [-1, 0, 1]]
# # print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)) #<---------- [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]




def threeNumberSum(arr, target):
    new_list = set()
    for i in arr:
        for j in arr:
            if i == j:
                continue
            third_num = target - (i + j)
            paired = [i, j]
            if third_num in arr:
                if third_num not in paired:
                    list_nums = [i, j, third_num]
                    new_list.add(tuple(sorted(list_nums)))
    new_list = [list(tup) for tup in new_list]
    return sorted(new_list)


print(threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0)) #<---------- [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-5, -1, 6], [-5, 0, 5], [-5, 2, 3], [-1, 0, 1]]
# print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)) #<---------- [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]









# def linkedList(head):
#     current_head = head.data
#     next_node = head.next
#     while current_head != None:
#         if current_head == next_node:
#             # skep over the dup value
#             next_node = next_node.next
#         else:
#             current_head = next_node
#         return current_head






