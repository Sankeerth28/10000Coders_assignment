# 1. Find the longest substring without repeating characters

def longest_substring(s):
    longest = ""
    current = ""

    for char in s:
        if char in current:
            current = current[current.index(char) + 1:]
        current += char

        if len(current) > len(longest):
            longest = current

    return longest


# 2. Two Sum

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        difference = target - num

        if difference in seen:
            return [seen[difference], i]

        seen[num] = i

    return []


# 3. Reverse a string without built-in functions

def reverse_string(s):
    result = ""

    for i in range(len(s) - 1, -1, -1):
        result += s[i]

    return result


# 4. Check if two strings are anagrams

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True


# 5. Find the first non-repeating character

def first_non_repeating(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in s:
        if count[char] == 1:
            return char

    return None


# 6. Move all zeros to the end

def move_zeros(nums):
    result = []

    for num in nums:
        if num != 0:
            result.append(num)

    while len(result) < len(nums):
        result.append(0)

    return result


# 7. Find the second largest element

def second_largest(nums):
    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    return second


# 8. Check if a number or string is a palindrome

def is_palindrome(value):
    s = str(value)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


# 9. Find duplicate elements in a list

def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


# 10. Flatten a nested list

def flatten_list(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


# 11. Implement stack and queue using lists

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None


# 12. Find the majority element

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    if nums.count(candidate) > len(nums) // 2:
        return candidate

    return None


# 13. Check for balanced parentheses

def balanced_parentheses(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


# 14. Implement binary search

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 15. Count frequency of elements using a dictionary

def frequency_count(items):
    frequency = {}

    for item in items:
        frequency[item] = frequency.get(item, 0) + 1

    return frequency


# Consecutive character occurrences
s = 'aabbaaccdd'

result = ""
count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

print(result)

# Output:
# a2b2a2c2d2