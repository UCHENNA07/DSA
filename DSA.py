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
#
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
#      def reverse(self):
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
#         This function returns the Kth node starting from the end of a linked list
#         Given this LinkedList: 1 -> 2 -> 3 -> 4 -> 5
#         If k=1 then return the first node from the end (the last node) which contains the value of 5.
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
#
# my_linked_list = LinkedList(3)
# my_linked_list.append(5)
# my_linked_list.append(4)
# my_linked_list.append(5)
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



# STACK AND QUEUES
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class Stack:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.top = new_node
#         self.height = 1
#
#     def print_stack(self):
#         temp = self.top
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#
#     def push(self, value):
#         new_node = Node(value)
#         if self.height == 0:
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#         self.height += 1
# #
#     def pop(self):
#         if self.height == 0:
#             return None
#         temp = self.top
#         self.top = self.top.next
#         temp.next = None
#         self.height -= 1
#         return temp


def is_valid_parentheses(s):
    # Create a new Stack to store opening parentheses
    stack = []
    # Mapping of closing to opening parentheses
    mapping = {')': '(', ']': '[', '}': '{'}
    # Iterate over each character in the string
    for char in s:
        # If char is a closing parenthesis
        if char in mapping:
            # Check if stack is empty or top of stack does not match opening parenthesis
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Push opening parenthesis onto the stack
            stack.append(char)
    # If the stack is empty, the parentheses are balanced
    return not stack


string1 = "()"
string2 = "{]"
print(is_valid_parentheses(string1))
print(is_valid_parentheses(string2))


# my_stack = Stack(3)
# my_stack.push(4)
# my_stack.push(5)
# my_stack.pop()
# my_stack.print_stack()


# QUEUES
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class Queue:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.first = new_node
#         self.last = new_node
#         self.length = 1
#
#     def print_queue(self):
#         temp = self.first
#         while temp:
#             print(temp.value)
#             temp = temp.next
#
#     def enqueue(self, value):
#         # This method appends a new node to the end of a queue
#         new_node = Node(value)
#         if self.length == 0:
#             self.first = new_node
#             self.last = new_node
#         else:
#             self.last.next = new_node
#             self.last = new_node
#         self.length += 1
#
#     def dequeue(self):
#         # This method removes the node at the beginning of the queue
#         if self.length == 0:
#             return None
#         temp = self.first
#         if self.length < 2:
#             self.first = None
#             self.last = None
#         else:
#             self.first = self.first.next
#             temp.next = None
#         self.length -= 1
#         return temp
#
#
# my_queue = Queue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# my_queue.dequeue()
# my_queue.print_queue()






