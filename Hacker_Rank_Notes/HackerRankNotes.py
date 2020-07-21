##############################################################################################################

# Equalize Array
def equalizeArray(arr):
    x = 2 #<--------------------from 0 to 2
    extraArr = []

    for i in arr:
        # 1
        AC = arr.count(i)
        # 2
        if AC >= x:
            x = AC
        elif AC < x:
            extraArr.append(i)
    # 3
    le = len(extraArr)
    print(le)
    return le

equalizeArray([1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 8, 8, 8])
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
# my_data = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
#
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
#     print(newList)
#     print(sum(newList))
#     return sum(newList)
#
# addingLowestNumbers(my_data)









# Balanced Brackets
# opening = ['[', '(', '{', '|']
# closing = [']', ')', '}', '|']
#
# def balancedBrackets(string):
#     for i in range(0, len(string)):
#         open_index = i
#         if i in opening:
#             for j in range(open_index + 1, len(string)):
#                 if j in closing:
#                     if opening.len(open_index) == closing.len(j):
#                         print('True')
#                     else:
#                         j += 1
#                 elif j == len(string)-1:
#                     print('False')
# balancedBrackets("yes, and yo{}u need to ma[]ke sure they don't overlap")









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
#             print("\nbiggerArr", biggerArr)
#             print("smallArr", smallArr)
#             print(f"Comparing *{biggerArr[x]}* from biggerB to *{smallArr[x]}* from smallA")
#             print("Letter removed list", poppedLetters)
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
#
#     return arr
#
# print(selection_sort([1, 7, 65, 4987, 55, 69, 87]))
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
#
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
#
#         else:
#             x += 1
#
# partitionArray(3, [1, 3, 2, 4, 6, 5, 7, 8])