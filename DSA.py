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



# TREES AND BINARY SEARCH TREES
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


    # This Recursion method is for binary search trees
    # This recursive contains method checks if a node(value) is contained in a binary search tree
    def recursive_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.recursive_contains(current_node.left, value)
        if value > current_node.value:
            return self.recursive_contains(current_node.right, value)

    def r_contains(self, value):
        return self.recursive_contains(self.root, value)

    def recursive_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.recursive_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.recursive_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.r_insert(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

    # TREE TRAVERSAL(Breadth First Search)
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results


    def DFS_Pre_Order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


    def DFS_Post_Order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results


    def DFS_In_Order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# print(my_tree.BFS())
# print(my_tree.DFS_Pre_Order())
# print(my_tree.DFS_Post_Order())
# print(my_tree.DFS_In_Order())

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
#
# print(my_tree.contains(27))
# print(my_tree.contains(4))
#
# print('BST Contains 27:')
# print(my_tree.r_contains(27))

# print('BST Contains 17:')
# print(my_tree.r_contains(17))
#
# print('Root:', my_tree.root.value)
# print('Root --> Left:', my_tree.root.left.value)
# print('Root --> Right:', my_tree.root.right.value)
#
# print(my_tree.min_value(my_tree.root))
# print(my_tree.min_value(my_tree.root.right))
#
# my_tree.delete_node(2)
#
# print('root:', my_tree.root.value)
# print('root.left:', my_tree.root.left.value)
# print('root.right:', my_tree.root.right)



# HASH TABLES
# Hash tables are deterministic which means we know the address and we can fetch any value based on our input
# While initializing a hash table, we create an address with a size of our choice
# class HashTable:
#     def __init__(self, size=7):
#         self.data_table = [None] * size
#
#     def hash(self, key):
#         my_hash = 0
#         for letter in key:
#             my_hash = (my_hash + ord(letter) * 23) % len(self.data_table)
#         return my_hash
#
#     def print_table(self):
#         for i, val in enumerate(self.data_table):
#             print(i, ": ", val)
#
#     def set_item(self, key, value):
#         index = self.hash(key)
#         if self.data_table[index] is None:
#             self.data_table[index] = []
#         self.data_table[index].append([key, value])

#     def get_item(self, key):
#         index = self.hash(key)
#         if self.data_table[index] is not None:
#             for i in range(len(self.data_table[index])):
#                 if self.data_table[index][i][0] == key:
#                     return self.data_table[index][i][1]
#         return None
#
#     def keys(self):
#         all_keys = []
#         for i in range(len(self.data_map)):
#             if self.data_map[i] is not None:
#                 for j in range(len(self.data_map[i])):
#                     all_keys.append(self.data_map[i][j][0])
#         return all_keys
#
#
# my_hash_table = HashTable()
# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)

# print(my_hash_table.get_item('bolts'))
# print(my_hash_table.get_item('washers'))
# print(my_hash_table.get_item('lumber'))
#
# print(my_hash_table.keys())

# my_hash_table.print_table()


#GRAPH
# class Graph:
#     def __init__(self):
#         self.graph = {}
#
#     def print_graph(self):
#         for vertex in self.graph:
#             print(vertex, ':', self.graph[vertex])
#
#     def add_vertex(self, vertex):
#         if vertex not in self.graph.keys():
#             self.graph[vertex] = []
#             return True
#         return False
#
#     def add_edge(self, v1, v2):
#         if v1 in self.graph.keys():
#             self.graph[v1].append(v2)
#         else:
#             self.graph[1] = [v2]
#
#         if v2 in self.graph:
#             self.graph[v2].append(v1)
#         else:
#             self.graph[v2] = [v1]
#
#     def remove_edge(self, v1, v2):
#         if v1 in self.graph.keys() and v2 in self.graph.keys():
#             try:
#                 self.graph[v1].remove(v2)
#                 self.graph[v2].remove(v1)
#             except ValueError:
#                 pass
#             return True
#         return False
#
#     def remove_vertex(self, vertex):
#         if vertex in self.graph.keys():
#             # we are looping through the items in the graph and removing the connections at each vertex
#             for other_vertex in self.graph[vertex]:
#                 self.graph[other_vertex].remove(vertex)
#             del self.graph[vertex]
#             return True
#         return False
#
#
# my_graph = Graph()
#
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
#
# my_graph.add_edge('A', 'B')
# my_graph.add_edge('A', 'C')
# my_graph.add_edge('A', 'D')
# my_graph.add_edge('B', 'D')
# my_graph.add_edge('C', 'D')
#
# # my_graph.remove_edge('A', 'D')
#
# my_graph.remove_vertex('D')
#
# my_graph.print_graph()


# HEAPS
# class MaxHeap:
#     def __init__(self):
#         self.heap = []
#
#     def left_child(self, index):
#         return 2 * index + 1
#
#     def right_child(self, index):
#         return 2 * index + 2
#
#     def parent(self, index):
#         return (index - 1) // 2
#
#     def swap(self, index1, index2):
#         self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
#
#     def insert(self, value):
#         self.heap.append(value)
#         current = len(self.heap) - 1
#
#         while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
#             self.swap(current, self.parent(current))
#             current = self.parent(current)
#
#     def sink_down(self, index):
#         max_index = index
#         while True:
#             left_index = self.left_child(index)
#             right_index = self.right_child(index)
#
#             if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
#                 max_index = left_index
#
#             if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
#                 max_index = right_index
#
#             if max_index != index:
#                 self.swap(index, max_index)
#                 index = max_index
#             else:
#                 return
#
#     def remove_item(self):
#         if len(self.heap) == 0:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
#
#         max_value = self.heap[0]
#         self.heap[0] = self.heap.pop()
#         self.sink_down(0)
#         return max_value
#
#     def insert_min_heap(self, value):
#         self.heap.append(value)
#         current = len(self.heap) - 1
#         while current > 0 and self.heap[current] < self.heap[self.parent(current)]:
#             self.swap(current, self.parent(current))
#             current = self.parent(current)
#
#     def remove_min_heap(self):
#         # If heap is empty, return None
#         if len(self.heap) == 0:
#             return None
#
#         # If heap has only one element, pop and return it
#         if len(self.heap) == 1:
#             return self.heap.pop()
#
#         # Store the minimum value (root of the min heap)
#         min_value = min(self.heap)
#
#         # Replace the root of the heap with the last element of the heap and then remove the last element
#         self.heap[0] = self.heap.pop()
#
#         # Restore the heap property by sinking down the new root
#         self.sink_down(0)
#
#         # Return the minimum value that has been removed
#         return min_value
#
#     def sink_down(self, index):
#         min_index = index
#         while True:
#             left_index = self.left_child(index)
#             right_index = self.right_child(index)
#
#             if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]:
#                 min_index = left_index
#
#             if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]:
#                 min_index = right_index
#
#             if min_index != index:
#                 self.swap(index, min_index)
#                 index = min_index
#             else:
#                 return
#
#
# my_heap = MaxHeap()
# my_heap.insert(99)
# my_heap.insert(75)
# my_heap.insert(80)
# my_heap.insert(55)
# my_heap.insert(60)
# my_heap.insert(50)
# my_heap.insert(65)
#
# print(my_heap.heap)
# #
# # my_heap.remove_item()
# #
# # print(my_heap.heap)
# #
# my_heap.insert_min_heap(4)
#
# print(my_heap.heap)
#
# removed = my_heap.remove_min_heap()
# print(f'Removed: {removed}, Heap: {my_heap.heap}')
#
# def find_kth_smallest(nums, k):
#     # Initialize a new MaxHeap
#     max_heap = MaxHeap()
#
#     # Loop over each number in the input list
#     for num in nums:
#         # Insert the current number into the heap. The heap maintains its properties automatically
#         max_heap.insert(num)
#
#         # If the heap size exceeds k, remove the maximum element. This keeps the heap size at k and ensures it
#         # only contains the smallest k numbers seen so far
#         if len(max_heap.heap) > k:
#             max_heap.remove_item()
#
#     # After the loop, the heap contains the smallest k numbers. The root of the heap is the kth smallest number,
#     # remove and return it as the function's result.
#     return max_heap.remove_item()
#
# nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
# ks = [2, 3, 4, 7]
# expected_outputs = [2, 3, 4, 5]
#
# for i in range(len(nums)):
#     print(f'Test case {i+1}...')
#     print(f'Input: {nums[i]} with k = {ks[i]}')
#     result = find_kth_smallest(nums[i], ks[i])
#     print(f'Output: {result}')
#     print(f'Expected output: {expected_outputs[i]}')
#     print(f'Test passed: {result == expected_outputs[i]}')
#     print('---------------------------------------')

#
# def stream_max(nums):
#     # Initialize an empty MaxHeap. This is a data structure where the parent node is always larger than or equal to
#     it's children.
#     max_heap = MaxHeap()
#
#     # Initialize an empty list to store the maximum numbers encountered so far while traversing the input list.
#     max_stream = []
#
#     # Iterate over each number in the input list.
#     for num in nums:
#         # Insert the current number into the MaxHeap. If this number is greater than the current maximum number in the
#         # heap, the heap will adjust itself so that this number becomes the new maximum
#         # (i.e., it moves to the root of the heap).
#         max_heap.insert(num)
#
#         # After each insertion, append the maximum value in the heap to the max_stream list. This value is always at
#         # the root of the heap and can be accessed using max_heap.heap[0]. As a result, max_stream[i] will always be
#         # the maximum value in nums up to index i.
#         max_stream.append(max_heap.heap[0])
#
#     # After we've finished the loop, return the max_stream list. This list represents the maximum number encountered
#     # so far for each position in the input list.
#     return max_stream
#
#
# test_cases = [
#     ([], []),
#     ([1], [1]),
#     ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
#     ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
#     ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
# ]
#
# for i, (nums, expected) in enumerate(test_cases):
#     result = stream_max(nums)
#     print(f'\nTest {i + 1}')
#     print(f'Input: {nums}')
#     print(f'Expected Output: {expected}')
#     print(f'Actual Output: {result}')
#     if result == expected:
#         print('Status: Passed')
#     else:
#         print('Status: Failed')


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






