# Data Structures and Algorithm

# Singly Linkedlist Constructor
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#
#     def print_list(self):
#         first = self.head
#         while first:
#             print(first.value)
#             first = first.next
#
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True
#
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while temp.next:
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
#
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#         return True
#
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return temp.value
#
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         # Temp is a variable we set and equal it to head because we would be looping through the list with temp.
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp.value
#
#     def set_value(self, index, value):
#         current = self.head
#         count = 0
#         while current:
#             if count == index:
#                 current.data = value
#                 return
#             current = current.next
#             count += 1
#         raise IndexError("Index out of range")
#
#     def insert(self, index, value):
#         new_node = Node(value)
#         if index == 0:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             current = self.head
#             count = 0
#             while current:
#                 if count == index - 1:
#                     new_node.next = current.next
#                     current.next = new_node
#                     return
#                 current = current.next
#                 count += 1
#
#             raise IndexError("Index out of range")
#
#     def remove_at_index(self, index):
#         if self.head is None:
#             return None
#         if index == 0:
#             self.head = self.head.next
#         else:
#             current = self.head
#             count = 0
#             while current:
#                 if count == index - 1:
#                     if current.next is None:
#                         return None
#                     current.next = current.next.next
#                     return
#                 current = current.next
#                 count += 1
#             return None
#
#     def reverse(self):
#         # We have to reverse head and tail, so we create a variable to do so.
#         temp = self.head
#         self.head = self.tail
#         self.tail = temp
#         # We now create two variables after at the right of temp and before at the left of temp
#         after = temp.next
#         before = None
#         # We now have to loop through the length of the list
#         for _ in range(self.length):
#             after = temp.next
#             temp.next = before
#             before = temp
#             temp = after
#
#     def find_middle_node(self):
#         # We create two variables slow and fast and set both of them to head
#         slow = self.head
#         fast = self.head
#         while fast is not None and fast.next is not None:
#             # Here, while the list is not empty and fast.next is not empty, the fast variable moves as twice as fast
#             # as the slow variable
#             slow = slow.next
#             fast = fast.next.next
#         return slow.value
#
#     def has_loop(self):
#         # Floyd's cycle-finding algorithm, also known as the "tortoise and hare" is similar to find_middle_node
#         # This function checks if theres a loop in the code and returns True or False
#         slow = self.head
#         fast = self.head
#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False
#
#     def find_kth_from_end(ll, k):
#         # This function returns the Kth node starting from the end of a linked list
#         # Given this LinkedList: 1 -> 2 -> 3 -> 4 -> 5
#         # If k=1 then return the first node from the end (the last node) which contains the value of 5.
#         slow = ll.head
#         fast = ll.head
#         for _ in range(k):
#             if fast is None:
#                 return None
#             fast = fast.next
#         while fast:
#             slow = slow.next
#             fast = fast.next
#         return slow
#
#     def reverse_between(self, m, n):
#         # This method takes two integers m and n and reversing the nodes in the linkedlist from index m to index n
#         # i.e. if you have a list of 1, 2, 3, 4, 5 and you want to reverse the nodes at index 2 and 4, your output will
#         # be 1, 2, 5, 4, 3
#         if self.head is None:
#             return False
#         before = Node(0)
#         before.next = self.head
#         prev = before
#         for i in range(m):
#             prev = prev.next
#         current = prev.next
#         for i in range(n - m):
#             temp = current.next
#             current.next = temp.next
#             temp.next = prev.next
#             prev.next = temp
#         self.head = before.next
#
#     def partition_list(self, x):
#         # In this method, we want to partition a list by giving an input(integer). Any number less than the input will
#         # be partitioned before the input and any number greater than the input will be partitioned after the input
#         # but maintaining the order in which the list was provided.
#         if not self.head:
#             return None
#         dummy1 = Node(0)
#         dummy2 = Node(0)
#         prev1 = dummy1
#         prev2 = dummy2
#         current = self.head
#         while current:
#             if current.value < x:
#                 prev1.next = current
#                 prev1 = current
#             else:
#                 prev2.next = current
#                 prev2 = current
#             current = current.next
#
#         prev2.next = None
#         prev1.next = dummy2.next
#         self.head = dummy1.next
#
#     def remove_duplicates(self):
#         values = set()
#         previous = None
#         first_element = self.head
#         while first_element:
#             if first_element.value in values:
#                 previous.next = first_element.next
#                 self.length -= 1
#             else:
#                 values.add(first_element.value)
#                 previous = first_element
#             first_element = first_element.next
#
#     def bubble_sort(self):
#         # Check if the list has less than 2 elements
#         if self.length < 2:
#             return
#
#         # Initialize the sorted_until pointer to None
#         sorted_until = None
#
#         # Continue sorting until sorted_until reaches the second node
#         while sorted_until != self.head.next:
#             # Initialize current pointer to head of the list
#             current = self.head
#
#             # Iterate through unsorted portion of the list until sorted_until
#             while current.next != sorted_until:
#                 next_node = current.next
#
#                 # Swap current and next_node values if current is greater
#                 if current.value > next_node.value:
#                     current.value, next_node.value = next_node.value, current.value
#
#                 # Move current pointer to next node
#                 current = current.next
#
#             # Update sorted_until pointer to the last node processed
#             sorted_until = current
#
#     # Define a method to sort a linked list in ascending order
#     # using the selection sort algorithm
#     def selection_sort(self):
#         # If the linked list has less than 2 elements, it is already sorted
#         if self.length < 2:
#             return
#
#         # Start with the first node as the current node
#         current = self.head
#
#         # While there is at least one more node after the current node
#         while current.next is not None:
#             # Assume the current node has the smallest value so far
#             smallest = current
#             # Start with the next node as the inner current node
#             inner_current = current.next
#
#             # Find the node with the smallest value among the remaining nodes
#             while inner_current is not None:
#                 if inner_current.value < smallest.value:
#                     smallest = inner_current
#                 inner_current = inner_current.next
#
#             # If the node with the smallest value is not the current node,
#             # swap their values
#             if smallest != current:
#                 current.value, smallest.value = smallest.value, current.value
#
#                 # Move to the next node
#             current = current.next
#
#         # Set the tail of the linked list to the last node processed
#         self.tail = current
#
#     def insertion_sort(self):
#         # Check if the length of the list is less than 2
#         if self.length < 2:
#             return
#
#         # Set the pointer to the first element of the sorted list
#         sorted_list_head = self.head
#
#         # Set the pointer to the second element of the list
#         unsorted_list_head = self.head.next
#
#         # Remove the first element from the sorted list
#         sorted_list_head.next = None
#
#         # Iterate through the unsorted list
#         while unsorted_list_head is not None:
#             # Save the current element
#             current = unsorted_list_head
#
#             # Move the pointer to the next element in the unsorted list
#             unsorted_list_head = unsorted_list_head.next
#
#             # Insert the current element into the sorted list
#             if current.value < sorted_list_head.value:
#                 # If the current element is smaller than the first element
#                 # in the sorted list, it becomes the new first element
#                 current.next = sorted_list_head
#                 sorted_list_head = current
#             else:
#                 # Otherwise, search for the appropriate position to insert the current element
#                 search_pointer = sorted_list_head
#                 while search_pointer.next is not None and current.value > search_pointer.next.value:
#                     search_pointer = search_pointer.next
#                 current.next = search_pointer.next
#                 search_pointer.next = current
#
#         # Update the head and tail of the list
#         self.head = sorted_list_head
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
#         self.tail = temp
#
#
#     # Method to merge a linked list with another linked list
#     def merge(self, other_list):
#         # Get the head node of the other linked list
#         other_head = other_list.head
#
#         # Create a dummy node to hold the merged list
#         dummy = Node(0)
#
#         # Set the current node to the dummy node
#         current = dummy
#
#         # Loop while both lists still have nodes
#         while self.head is not None and other_head is not None:
#
#             # Compare the values of the first nodes in each list
#             if self.head.value < other_head.value:
#                 # If the value in the first list is smaller,
#                 # add it to the current node and move to the next node in the first list
#                 current.next = self.head
#                 self.head = self.head.next
#             else:
#                 # Otherwise, add the value from the second list
#                 # and move to the next node in the second list
#                 current.next = other_head
#                 other_head = other_head.next
#
#             # Move the current node to the next position
#             current = current.next
#
#         # If the first list still has nodes left, add them to the current node
#         if self.head is not None:
#             current.next = self.head
#         else:
#             # If the second list still has nodes left, add them to the current node
#             current.next = other_head
#             # Update the tail of the merged list to be the tail of the second list
#             self.tail = other_list.tail
#
#         # Set the head of the merged list to the next node after the dummy node
#         self.head = dummy.next
#
#         # Update the length of the merged list
#         self.length += other_list.length
#
#
# my_linked_list = LinkedList(3)
# my_linked_list.append(5)
# my_linked_list.append(4)
# my_linked_list.append(6)
# my_linked_list.append(10)

# my_linked_list.pop()
# my_linked_list.prepend(1)
# my_linked_list.pop_first()
# print(my_linked_list.get(2))
# my_linked_list.set_value(1, 5)
# my_linked_list.insert(1, 2)
# my_linked_list.remove_at_index(2)
# my_linked_list.reverse()
# print(my_linked_list.find_middle_node())
# print(my_linked_list.has_loop())

# k = 2
# result = my_linked_list.find_kth_from_end(k)
# print(result.value)
# my_linked_list.reverse_between(2, 4)
# my_linked_list.partition_list(5)
# my_linked_list.remove_duplicates()

# my_linked_list.print_list()


# print("Linked List Before Sort:")
# my_linked_list.print_list()
#
# my_linked_list.bubble_sort()
#
# print("\nSorted Linked List:")
# my_linked_list.print_list()


# print("Linked List Before Sort:")
# my_linked_list.print_list()
#
# my_linked_list.selection_sort()
#
# print("\nSorted Linked List:")
# my_linked_list.print_list()


# print("Linked List Before Sort:")
# my_linked_list.print_list()
#
# my_linked_list.insertion_sort()
#
# print("\nSorted Linked List:")
# my_linked_list.print_list()

