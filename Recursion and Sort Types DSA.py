# Recursion
# It is a function that calls itself until it doesn't
# def open_box():
#     if ball:
#         return ball
#     open_box()

# STACK
# def funcThree():
#     print('Three')
#
# def funcTwo():
#     funcThree()
#     print('Two')
#
# def funcOne():
#     funcTwo()
#     print('One')
#
# funcOne()


# FACTORIAL
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(4))



# BUBBLE SORT
# def bubble_sort(my_list):
#     for i in range(len(my_list) -1, 0, -1):
#         for j in range(i):
#             if my_list[j] > my_list[j+1]:
#                 # swap two items
#                 temp = my_list[j]
#                 my_list[j] = my_list[j+1]
#                 my_list[j+1] = temp
#     return my_list
#
#
# print(bubble_sort([3, 1, 4, 2, 6, 5]))


# For selection sort, we need the index of the items in the list
# def selection_sort(my_list):
#     for i in range(len(my_list) -1):
#         min_index = i
#         for j in range(i+1, len(my_list)):
#             if my_list[j] < my_list[min_index]:
#                 min_index = j
#         # We will only swap the two items if they are not equal
#         if i != min_index:
#             temp = my_list[i]
#             my_list[i] = my_list[min_index]
#             my_list[min_index] = temp
#     return my_list
#
#
# print(selection_sort([4, 2, 6, 5, 1, 3]))


# def insertion_sort(my_list):
#     # for insertion sort, we start from the second item on the list i.e. the item at index of 1
#     for i in range(1, len(my_list)):
#         temp = my_list[i]
#         j = i-1
#         while temp < my_list[j] and j > -1:
#             my_list[j+1] = my_list[j]
#             my_list[j] = temp
#             j -= 1
#     return my_list
#
#
# print(insertion_sort([4, 2, 6, 5, 1, 3]))


# def bubble_sort(self):
#     # Check if the list has less than 2 elements
#     if self.length < 2:
#         return
#
#     # Initialize the sorted_until pointer to None
#     sorted_until = None
#
#     # Continue sorting until sorted_until reaches the second node
#     while sorted_until != self.head.next:
#         # Initialize current pointer to head of the list
#         current = self.head
#
#         # Iterate through unsorted portion of the list until sorted_until
#         while current.next != sorted_until:
#             next_node = current.next
#
#             # Swap current and next_node values if current is greater
#             if current.value > next_node.value:
#                 current.value, next_node.value = next_node.value, current.value
#
#             # Move current pointer to next node
#             current = current.next
#
#         # Update sorted_until pointer to the last node processed
#         sorted_until = current
#
#
# my_linked_list = LinkedList(4)
# my_linked_list.append(2)
# my_linked_list.append(6)
# my_linked_list.append(5)
# my_linked_list.append(1)
# my_linked_list.append(3)
#
# print("Linked List Before Sort:")
# my_linked_list.print_list()
#
# my_linked_list.bubble_sort()
#
# print("\nSorted Linked List:")
# my_linked_list.print_list()



# MERGE SORT
# It's' merging two sorted list and sorts them
# def merge(list1, list2):
#     combined = []  # initialize an empty list to store the merged result
#     i = 0  # initialize the index of list1 to zero
#     j = 0  # initialize the index of list2 to zero
#     while i < len(list1) and j < len(list2):
#         # compare the current elements of list1 and list2, and append the smaller one to combined
#         if list1[i] < list2[j]:
#             combined.append(list1[i])
#             i += 1
#         else:
#             combined.append(list2[j])
#             j += 1
#     # if there are any remaining elements in list1, add them to combined
#     while i < len(list1):
#         combined.append(list1[i])
#         i += 1
#     # if there are any remaining elements in list2, add them to combined
#     while j < len(list2):
#         combined.append(list2[j])
#         j += 1
#     return combined  # return the merged and sorted list
#
#
# # print(merge([1, 2, 7, 8], [3, 4, 5, 6]))
#
#
# def merge_sort(my_list):
#     # if the list contains only one element, it is already sorted
#     if len(my_list) == 1:
#         return my_list
#
#     # find the midpoint index of the list
#     mid_index = int(len(my_list) / 2)
#
#     # recursively sort the left and right halves of the list
#     left = merge_sort(my_list[:mid_index])
#     right = merge_sort(my_list[mid_index:])
#
#     # merge the sorted left and right halves of the list
#     return merge(left, right)
#
#
# original_list = [3, 2, 1, 4]
# sorted_list = merge_sort(original_list)
# print('Original List:', original_list)
# print('\nSorted List:', sorted_list)

# Note: Merge Sort algorithms Big O is 0(n log n) and its efficient



# QUICK SORT
# def swap(my_list, index1, index2):
#     temp = my_list[index1]
#     my_list[index1] = my_list[index2]
#     my_list[index2] = temp
#
#
# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index
#     for i in range(pivot_index + 1, end_index + 1):
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             swap(my_list, swap_index, i)
#     swap(my_list, pivot_index, swap_index)
#     return swap_index
#
#
# def quick_sort_helper(my_list, left, right):
#     if left < right:
#         pivot_index = pivot(my_list, left, right)
#         quick_sort_helper(my_list, left, pivot_index - 1)
#         quick_sort_helper(my_list, pivot_index + 1, right)
#     return my_list
#
#
# def quick_sort(my_list):
#     return quick_sort_helper(my_list, 0, len(my_list) - 1)
#
#
# print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
# # Note: Quick Sort algorithms Big O is 0(n log n) and its efficient





