# HEAPS
class MaxHeap:
    def __init__(self):
        self.heap = []

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index - 1) // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def sink_down(self, index):
        max_index = index
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return

    def remove_item(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        return max_value

    def insert_min_heap(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove_min_heap(self):
        # If heap is empty, return None
        if len(self.heap) == 0:
            return None

        # If heap has only one element, pop and return it
        if len(self.heap) == 1:
            return self.heap.pop()

        # Store the minimum value (root of the min heap)
        min_value = min(self.heap)

        # Replace the root of the heap with the last element of the heap and then remove the last element
        self.heap[0] = self.heap.pop()

        # Restore the heap property by sinking down the new root
        self.sink_down(0)

        # Return the minimum value that has been removed
        return min_value

    def sink_down(self, index):
        min_index = index
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]:
                min_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]:
                min_index = right_index

            if min_index != index:
                self.swap(index, min_index)
                index = min_index
            else:
                return


my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)

print(my_heap.heap)
#
# my_heap.remove_item()
#
# print(my_heap.heap)
#
my_heap.insert_min_heap(4)

print(my_heap.heap)

removed = my_heap.remove_min_heap()
print(f'Removed: {removed}, Heap: {my_heap.heap}')


def find_kth_smallest(nums, k):
    # Initialize a new MaxHeap
    max_heap = MaxHeap()

    # Loop over each number in the input list
    for num in nums:
        # Insert the current number into the heap. The heap maintains its properties automatically
        max_heap.insert(num)

        # If the heap size exceeds k, remove the maximum element. This keeps the heap size at k and ensures it
        # only contains the smallest k numbers seen so far
        if len(max_heap.heap) > k:
            max_heap.remove_item()

    # After the loop, the heap contains the smallest k numbers. The root of the heap is the kth smallest number,
    # remove and return it as the function's result.
    return max_heap.remove_item()

nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f'Test case {i+1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')


def stream_max(nums):
    # Initialize an empty MaxHeap. This is a data structure where the parent node is always larger than or equal to
    it's children.
    max_heap = MaxHeap()

    # Initialize an empty list to store the maximum numbers encountered so far while traversing the input list.
    max_stream = []

    # Iterate over each number in the input list.
    for num in nums:
        # Insert the current number into the MaxHeap. If this number is greater than the current maximum number in the
        # heap, the heap will adjust itself so that this number becomes the new maximum
        # (i.e., it moves to the root of the heap).
        max_heap.insert(num)

        # After each insertion, append the maximum value in the heap to the max_stream list. This value is always at
        # the root of the heap and can be accessed using max_heap.heap[0]. As a result, max_stream[i] will always be
        # the maximum value in nums up to index i.
        max_stream.append(max_heap.heap[0])

    # After we've finished the loop, return the max_stream list. This list represents the maximum number encountered
    # so far for each position in the input list.
    return max_stream


test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i + 1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')


