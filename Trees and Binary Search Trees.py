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

    def is_valid_bst(self):
        # Get node values of the binary search tree in ascending order
        node_values = self.dfs_in_order()
        # Iterate through the node values using a for loop
        for i in range(1, len(node_values)):
            # Check if each node value is greater than the previous node value
            if node_values[i] <= node_values[i - 1]:
                # If node values are not sorted in ascending order, the binary
                # search tree is not valid, so return False
                return False
        # If all node values are sorted in ascending order, the binary search tree
        # is a valid binary search tree, so return True
        return True

    def kth_smallest(self, k):
        # initialize the number of nodes visited to 0
        self.kth_smallest_count = 0
        # call the helper function with the root node and k
        return self.kth_smallest_helper(self.root, k)

    def kth_smallest_helper(self, node, k):
        if node is None:
            # if the current node is None, return None
            return None

        # recursively call the helper function on the left child of the node and store the result in left_result
        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            # if left_result is not None, return it
            return left_result

        # increment the number of nodes visited by 1
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            # if the kth smallest element is found, return the value of the current node
            return node.value

        # recursively call the helper function on the right child of the node and store the result in right_result
        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            # if right_result is not None, return it
            return right_result

        # if the kth smallest element is not found, return None
        return None


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())
print(my_tree.DFS_Pre_Order())
print(my_tree.DFS_Post_Order())
print(my_tree.DFS_In_Order())

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.contains(27))
print(my_tree.contains(4))

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('BST Contains 17:')
print(my_tree.r_contains(17))

print('Root:', my_tree.root.value)
print('Root --> Left:', my_tree.root.left.value)
print('Root --> Right:', my_tree.root.right.value)

print(my_tree.min_value(my_tree.root))
print(my_tree.min_value(my_tree.root.right))

my_tree.delete_node(2)

print('root:', my_tree.root.value)
print('root.left:', my_tree.root.left.value)
print('root.right:', my_tree.root.right)

