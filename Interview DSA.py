# This second method is the most efficient way to code this because its O(n)
def items_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(items_in_common(list1, list2))


def find_duplicates(nums):
    # create an empty hash table
    num_counts = {}
    # iterate through each number in the array
    for num in nums:
        # add the number to the hash table or increment its count if it's already in the hash table
        num_counts[num] = num_counts.get(num, 0) + 1
    # create a list of the numbers that appear more than once in the input array
    duplicates = [num for num, count in num_counts.items() if count > 1]
    # return the list of duplicates
    return duplicates


nums = [1, 2, 3, 4, 5, 5, 4, 3]
print(find_duplicates(nums))


def first_non_repeating_char(string):
    # create an empty hash table to count the frequency of each character
    char_counts = {}
    # count the frequency of each character in the string
    for char in string:
        # this increments the count by 1 in the dictionary
        char_counts[char] = char_counts.get(char, 0) + 1
    # find the first non-repeating character in the string
    for char in string:
        if char_counts[char] == 1:
            return char
    # return None if no non-repeating character is found
    return None


print(first_non_repeating_char('Leetcode'))


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


def group_anagrams(strings):
    # create an empty hash table
    anagram_groups = {}

    # iterate through each string in the array
    for string in strings:
        # sort each string to get its sorted_string form
        # sorted('eat') returns ['a', 'e', 't']
        # ''.join(['a', 'e', 't']) coverts the array of chars to 'aet' string

        sorted_string = ''.join(sorted(string))
        # check to see if the sorted_string form of the string exists in the hash table
        if sorted_string in anagram_groups:
            # if it does then add the string there
            anagram_groups[sorted_string].append(string)
        else:
            # otherwise create new sorted_string form and add the string there
            anagram_groups[sorted_string] = [string]
    # convert the hash table to a list of lists
    return list(anagram_groups.values())

print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def two_sum(nums, target):
    # create an empty hash table
    num_map = {}

    # iterate through each number in the array
    for i, num in enumerate(nums):
        # calculate the complement of the current number
        complement = target - num

        # check if the complement is in the hash table
        if complement in num_map:
            # if it is, return the indexes of the two numbers
            return [num_map[complement], i]

        # add the current number and its index to the hash table
        num_map[num] = i

    # if no two numbers add up to the target, return an empty list
    return []


print(two_sum([2, 7, 11, 15], 9))


def subarray_sum(nums, target):
    # Dictionary to store the running sums (keys) and their corresponding (values).
    sum_index = {0: -1}

    # Variable to keep track of the current running sum.
    current_sum = 0

    # Iterate through the list with both index and value.
    for i, num in enumerate(nums):
        # Add the current number to the running sum.
        current_sum += num

        # Check if there's a subarray sum that matches the target.
        if current_sum - target in sum_index:
            # If there's a match, we return the start and end indices of that subarray.
            #'sum_index[current_sum - target] + 1' gives the start index of the subarray: It accesses the index stored
            # in sum_index where the subarray begins (current_sum - target). We add 1 because Python is 0-indexed and
            # we want the first element of the subarray, not the element before it. 'i' gives the end index of the
            # subarray: It's the current index in the loop, where the subarray ends  as the cumulative sum up to this
            # index equals the target when we subtract the sum at the start of the subarray.
            return [sum_index[current_sum - target] + 1, i]

        # If no subarray sum has been found, store the current running sum and its corresponding index.
        sum_index[current_sum] = i

    # If no subarray sum is found after iterating through the entire list, return an empty list.
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))


We are removing duplicates using the SET keyword
def remove_duplicates(my_list):
    new_list = list(set(my_list))
    return new_list

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)


def has_unique_chars(string):
    # Create an empty set to store characters
    char_set = set()
    # Loop through each character in the string
    for char in string:
        # Check if the character is already in the set
        if char in char_set:
            # If it is, return False (the string has duplicate characters)
            return False
        # If the character is not in the set, add it to the set
        char_set.add(char)
    # If we get to the end of the string without finding duplicates, return True
    return True


print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False


def find_pairs(arr1, arr2, target):
    # Convert arr1 to a set
    set1 = set(arr1)
    # Initialize an empty list to store the pairs
    pairs = []
    # Loop through each number in arr2
    for num in arr2:
        # Calculate the complement of the current number
        complement = target - num
        # Check if the complement is in set1
        if complement in set1:
            # If it is, add the pair to the pairs list
            pairs.append((complement, num))
    # Return the list of pairs that add up to the target value
    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7
pairs = find_pairs(arr1, arr2, target)
print(pairs)


def longest_consecutive_sequence(nums):
    # Create a set to keep track of the numbers in the array
    num_set = set(nums)
    longest_sequence = 0

    # Loop through the numbers in the nums array
    for num in nums:
        # Check if the current number is the start of a new sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            # Keep incrementing the current number until the end of the sequence is reached
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            # Update the longest sequence if the current sequence is longer
            longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))


def max_earnings(earning_per_fight):
    num_fight = len(earning_per_fight)
    if num_fight == 0:
        return 0
    if num_fight == 1:
        return 0

    dp = [0] * num_fight
    dp[0] = earning_per_fight[0]
    dp[1] = earning_per_fight[1]

    for i in range(1, num_fight):
        dp[i] = max(earning_per_fight[i] + dp[i - 2], dp[i - 1])
    return dp[num_fight - 1]


earning_per_fight = [6, 2, 5, 94]

print(max_earnings(earning_per_fight))


def count_divisible_by_5(number_list):
    divisible_numbers = []
    for num in number_list:
        if num % 5 == 0:
            divisible_numbers.append(num)

    return len(divisible_numbers)


numbers = [10, 15, 20, 25, 30]
print(count_divisible_by_5(numbers))


def remove_element(nums, val):
    # Initialize the index variable to 0
    i = 0

    # Iterate through the array using a while loop
    while i < len(nums):
        # Check if the current element is equal to the given value
        if nums[i] == val:
            # If equal, remove the element in-place using pop()
            nums.pop(i)
        else:
            # If not equal, increment the index to move to the next element
            i += 1

    # Return the new length of the modified array
    return len(nums)

# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("BEFORE:", nums1)
new_length1 = remove_element(nums1, val1)
print("AFTER:", nums1, "\nNew length:", new_length1)


def find_max_min(my_List):
    # Initialize the maximum and minimum variables
    # to the first element of the list
    maximum = minimum = my_List[0]
    # Traverse the list and update the
    # maximum and minimum variables
    for num in my_List:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num

    # Return the maximum and minimum variables
    return maximum, minimum


print(find_max_min([5, 3, 8, 1, 6, 9]))


def find_longest_string(string_list):
    # Initialize the variable to store the longest string to an empty string
    longest_string = ""
    # Loop through each string in the list of strings
    for string in string_list:
        # Check if the length of the current string is greater than the
        # length of the current longest string
        if len(string) > len(longest_string):
            # If so, update the longest string to be the current string
            longest_string = string
    # Return the longest string
    return longest_string

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)


def remove_duplicates(nums):
    # Return 0 if input list is empty
    if not nums:
        return 0

    # Initialize write_pointer at index 1
    write_pointer = 1

    # Loop through list starting from index 1
    for read_pointer in range(1, len(nums)):
        # Check if current element is unique
        if nums[read_pointer] != nums[read_pointer - 1]:
            # Move unique element to write_pointer
            nums[write_pointer] = nums[read_pointer]
            # Increment write_pointer for next unique element
            write_pointer += 1

    # Return new length of list with unique elements
    return write_pointer


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


def max_profit(prices):
    # Initialize min_price to positive infinity
    min_price = float('inf')
    # Initialize max_profit to 0
    max_profit = 0

    # Iterate through the list of stock prices
    for price in prices:
        # Update min_price with the lowest price so far
        min_price = min(min_price, price)
        # Calculate profit by selling at the current price
        profit = price - min_price
        # Update max_profit with the highest profit so far
        max_profit = max(max_profit, profit)

    # Return the maximum profit after iterating
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)


def rotate(nums, k):
    # Calculate the effective number of steps to rotate
    k = k % len(nums)
    # Rearrange the elements in the rotated order
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


def max_subarray(nums):
    # Return 0 if input list is empty
    if not nums:
        return 0

    # Initialize max_sum and current_sum
    max_sum = current_sum = nums[0]

    # Iterate through the remaining elements
    for num in nums[1:]:
        # Update current_sum
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)

    # Return the maximum subarray sum
    return max_sum


# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)



