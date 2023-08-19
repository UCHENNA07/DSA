# DOUBLY LINKED LISTS
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# class DoublyLinkedList:
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
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1
#         return True
#
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.tail
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             temp.prev = None
#         self.length -= 1
#         return temp
#
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         new_node.next = self.head
#         self.head.prev = new_node
#         self.head = new_node
#         self.length += 1
#         return True
#
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#             temp.next = None
#         self.length -= 1
#         return temp
#
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         if index < self.length/2:
#             for _ in range(index):
#                 temp = temp.next
#         else:
#             temp = self.tail
#             for _ in range(self.length - 1, index, -1):
#                 temp = temp.prev
#         return temp
#
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
#
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#         new_node = Node(value)
#         before = self.get(index - 1)
#         after = before.next
#         new_node.prev = before
#         new_node.next = after
#         before.next = new_node
#         after.prev = new_node
#         self.length += 1
#         return True
#
#     def remove(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         if index == 0:
#             return self.pop_first()
#         if index == self.length - 1:
#             return self.pop()
#         temp = self.get(index)
#         temp.next.prev = temp.prev
#         temp.prev.next = temp.next
#         temp.next = None
#         temp.prev = None
#         self.length -= 1
#         return temp
#
#     def swap_first_last(self):
#         # This method switches the values at the first and last node of a list i.e. 1, 2, 3 ,4 to 4, 2, 3, 1
#         if self.length < 2:
#             return None
#         temp = self.head
#         self.head.value, self.tail.value = self.tail.value, self.head.value
#         return temp
#
#     def reverse(self):
#         # This method reverses the arrangement of the nodes
#         if self.length < 2:
#             return None
#         temp = self.head
#         self.head.value, self.tail.value = self.tail.value, self.head.value
#         self.head.next.value, self.tail.prev.value = self.tail.prev.value, self.head.next.value
#         return temp
#
#     def is_palindrome(self):
#         # This method returns True if a doubly linkedlist list reads the same forwards and backwards.
#         if self.length < 2:
#             return True
#         first = self.head
#         last = self.tail
#         for _ in range(self.length):
#             if first.value != last.value:
#                 return False
#             first = first.next
#             last = last.prev
#         return True
#
#     def swap_pairs(self):
#         dummy = Node(0)
#         dummy.next = self.head
#         prev = dummy
#         while self.head and self.head.next:
#             first_node = self.head
#             second_node = self.head.next
#             prev.next = second_node
#             first_node.next = second_node.next
#             second_node.next = first_node
#             second_node.prev = prev
#             first_node.prev = second_node
#             if first_node.next:
#                 first_node.next.prev = first_node
#             self.head = first_node.next
#             prev = first_node
#         self.head = dummy.next
#         if self.head:
#             self.head.prev = None
#
#
# my_doubly_linked_list = DoublyLinkedList(4)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(4)
#my_doubly_linked_list.pop()
#my_doubly_linked_list.prepend(1)
#my_doubly_linked_list.pop_first()
#print(my_doubly_linked_list.get(1))
#my_doubly_linked_list.set_value(2, 10)
#my_doubly_linked_list.insert(1, 2)
#my_doubly_linked_list.remove(1)
#my_doubly_linked_list.swap_first_last()
#my_doubly_linked_list.reverse()
#print(my_doubly_linked_list.is_palindrome())
#my_doubly_linked_list.swap_pairs()
#my_doubly_linked_list.print_list()