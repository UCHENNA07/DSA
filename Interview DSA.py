# This second method is the most efficient way to code this because its O(n)
# def items_in_common(list1, list2):
#     my_dict = {}
#     for i in list1:
#         my_dict[i] = True
#     for j in list2:
#         if j in my_dict:
#             return True
#     return False
#
#
# list1 = [1, 3, 5]
# list2 = [2, 4, 5]
#
# print(items_in_common(list1, list2))


# def find_duplicates(nums):
#     # create an empty hash table
#     num_counts = {}
#     # iterate through each number in the array
#     for num in nums:
#         # add the number to the hash table or increment its count if it's already in the hash table
#         num_counts[num] = num_counts.get(num, 0) + 1
#     # create a list of the numbers that appear more than once in the input array
#     duplicates = [num for num, count in num_counts.items() if count > 1]
#     # return the list of duplicates
#     return duplicates
#
#
# nums = [1, 2, 3, 4, 5, 5, 4, 3]
# print(find_duplicates(nums))


# def first_non_repeating_char(string):
#     # create an empty hash table to count the frequency of each character
#     char_counts = {}
#     # count the frequency of each character in the string
#     for char in string:
#         # this increments the count by 1 in the dictionary
#         char_counts[char] = char_counts.get(char, 0) + 1
#     # find the first non-repeating character in the string
#     for char in string:
#         if char_counts[char] == 1:
#             return char
#     # return None if no non-repeating character is found
#     return None
#
#
# print(first_non_repeating_char('Leetcode'))


# def group_anagrams(strings):
#     # create an empty hash table
#     anagram_groups = {}
#
#     # iterate through each string in the array
#     for string in strings:
#         # sort each string to get its sorted_string form
#         # sorted('eat') returns ['a', 'e', 't']
#         # ''.join(['a', 'e', 't']) coverts the array of chars to 'aet' string
#
#         sorted_string = ''.join(sorted(string))
#         # check to see if the sorted_string form of the string exists in the hash table
#         if sorted_string in anagram_groups:
#             # if it does then add the string there
#             anagram_groups[sorted_string].append(string)
#         else:
#             # otherwise create new sorted_string form and add the string there
#             anagram_groups[sorted_string] = [string]
#     # convert the hash table to a list of lists
#     return list(anagram_groups.values())
#
# print("1st set:")
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# def two_sum(nums, target):
#     # create an empty hash table
#     num_map = {}
#
#     # iterate through each number in the array
#     for i, num in enumerate(nums):
#         # calculate the complement of the current number
#         complement = target - num
#
#         # check if the complement is in the hash table
#         if complement in num_map:
#             # if it is, return the indexes of the two numbers
#             return [num_map[complement], i]
#
#         # add the current number and its index to the hash table
#         num_map[num] = i
#
#     # if no two numbers add up to the target, return an empty list
#     return []
#
#
# print(two_sum([2, 7, 11, 15], 9))


# def subarray_sum(nums, target):
#     # Dictionary to store the running sums (keys) and their corresponding (values).
#     sum_index = {0: -1}
#
#     # Variable to keep track of the current running sum.
#     current_sum = 0
#
#     # Iterate through the list with both index and value.
#     for i, num in enumerate(nums):
#         # Add the current number to the running sum.
#         current_sum += num
#
#         # Check if there's a subarray sum that matches the target.
#         if current_sum - target in sum_index:
#             # If there's a match, we return the start and end indices of that subarray.
#             #'sum_index[current_sum - target] + 1' gives the start index of the subarray: It accesses the index stored
#             # in sum_index where the subarray begins (current_sum - target). We add 1 because Python is 0-indexed and
#             # we want the first element of the subarray, not the element before it. 'i' gives the end index of the
#             # subarray: It's the current index in the loop, where the subarray ends  as the cumulative sum up to this
#             # index equals the target when we subtract the sum at the start of the subarray.
#             return [sum_index[current_sum - target] + 1, i]
#
#         # If no subarray sum has been found, store the current running sum and its corresponding index.
#         sum_index[current_sum] = i
#
#     # If no subarray sum is found after iterating through the entire list, return an empty list.
#     return []
#
#
# nums = [1, 2, 3, 4, 5]
# target = 9
# print(subarray_sum(nums, target))

# We are removing duplicates using the SET keyword
# def remove_duplicates(my_list):
#     new_list = list(set(my_list))
#     return new_list
#
#
# my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
# new_list = remove_duplicates(my_list)
# print(new_list)


# def has_unique_chars(string):
#     # Create an empty set to store characters
#     char_set = set()
#     # Loop through each character in the string
#     for char in string:
#         # Check if the character is already in the set
#         if char in char_set:
#             # If it is, return False (the string has duplicate characters)
#             return False
#         # If the character is not in the set, add it to the set
#         char_set.add(char)
#     # If we get to the end of the string without finding duplicates, return True
#     return True
#
#
# print(has_unique_chars('abcdefg')) # should return True
# print(has_unique_chars('hello')) # should return False


# def find_pairs(arr1, arr2, target):
#     # Convert arr1 to a set
#     set1 = set(arr1)
#     # Initialize an empty list to store the pairs
#     pairs = []
#     # Loop through each number in arr2
#     for num in arr2:
#         # Calculate the complement of the current number
#         complement = target - num
#         # Check if the complement is in set1
#         if complement in set1:
#             # If it is, add the pair to the pairs list
#             pairs.append((complement, num))
#     # Return the list of pairs that add up to the target value
#     return pairs
#
#
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 4, 6, 8, 10]
# target = 7
# pairs = find_pairs(arr1, arr2, target)
# print(pairs)


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


