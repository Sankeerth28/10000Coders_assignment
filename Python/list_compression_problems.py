# ==============================
# LIST COMPREHENSION PROBLEMS
# ==============================

# 1. Create a list of squares of numbers from 1 to 20
squares = [x ** 2 for x in range(1, 21)]
print("1.", squares)


# 2. Generate a list of even numbers between 1 and 50
even_numbers = [x for x in range(1, 51) if x % 2 == 0]
print("2.", even_numbers)


# 3. Generate a list of odd numbers between 1 and 50
odd_numbers = [x for x in range(1, 51) if x % 2 != 0]
print("3.", odd_numbers)


# 4. Numbers divisible by both 3 and 5 from 1 to 100
numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print("4.", numbers)


# 5. Extract all vowels from "comprehension"
word = "comprehension"
vowels = [x for x in word if x in "aeiou"]
print("5.", vowels)


# 6. Words with more than 3 letters
words = ["cat", "dog", "parrot", "cow"]
result = [word for word in words if len(word) > 3]
print("6.", result)


# 7. ASCII values of characters in "Python"
word = "Python"
ascii_values = [ord(x) for x in word]
print("7.", ascii_values)


# 8. Prime numbers between 10 and 50
primes = [
    x for x in range(10, 51)
    if x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
]
print("8.", primes)


# 9. (number, square) tuples for numbers from 5 to 10
result = [(x, x ** 2) for x in range(5, 11)]
print("9.", result)


# 10. Names starting with 'A' or 'a'
names = ["Alice", "bob", "Anil", "David", "arjun", "John"]
result = [name for name in names if name.startswith(("A", "a"))]
print("10.", result)


# 11. Flatten a 2D list
numbers = [[1, 2], [3, 4], [5, 6]]
result = [x for row in numbers for x in row]
print("11.", result)


# 12. Add elements of two lists element-wise
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = [a + b for a, b in zip(list1, list2)]
print("12.", result)


# 13. Find palindrome words
words = ["level", "python", "madam", "world", "racecar"]
palindromes = [word for word in words if word == word[::-1]]
print("13.", palindromes)


# 14. Product of pairs
list1 = [2, 4, 6]
list2 = [1, 3, 5]
result = [i * j for i in list1 for j in list2]
print("14.", result)


# ==============================
# TUPLE COMPREHENSION PROBLEMS
# ==============================
# Note: Python does not have true tuple comprehensions.
# We use generator expressions with tuple().


# 1. Tuple of squares from 1 to 15
squares = tuple(x ** 2 for x in range(1, 16))
print("Tuple 1.", squares)


# 2. Tuple of odd numbers from 1 to 15
odd_numbers = tuple(x for x in range(1, 16) if x % 2 != 0)
print("Tuple 2.", odd_numbers)


# 3. Numbers divisible by both 3 and 5 between 1 and 50
numbers = tuple(x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0)
print("Tuple 3.", numbers)


# 4. Extract vowels from "comprehension"
word = "comprehension"
vowels = tuple(x for x in word if x in "aeiou")
print("Tuple 4.", vowels)


# 5. Words with more than 3 letters
words = ["cat", "dog", "parrot", "cow"]
result = tuple(word for word in words if len(word) > 3)
print("Tuple 5.", result)


# 6. ASCII values of characters in "Python"
word = "Python"
ascii_values = tuple(ord(x) for x in word)
print("Tuple 6.", ascii_values)


# 7. Prime numbers between 10 and 50
primes = tuple(
    x for x in range(10, 51)
    if x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
)
print("Tuple 7.", primes)


# 8. (number, square) pairs for numbers from 5 to 10
result = tuple((x, x ** 2) for x in range(5, 11))
print("Tuple 8.", result)


# 9. Names starting with 'A' or 'a'
names = ["Alice", "bob", "Anil", "David", "arjun", "John"]
result = tuple(name for name in names if name.startswith(("A", "a")))
print("Tuple 9.", result)


# 10. Flatten a 2D list into a tuple
numbers = [[1, 2], [3, 4], [5, 6]]
result = tuple(x for row in numbers for x in row)
print("Tuple 10.", result)


# 11. Add elements of two lists element-wise and store in tuple
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = tuple(a + b for a, b in zip(list1, list2))
print("Tuple 11.", result)


# 12. Find palindrome words and store them in a tuple
words = ["level", "python", "madam", "world", "racecar"]
palindromes = tuple(word for word in words if word == word[::-1])
print("Tuple 12.", palindromes)


# 13. Product of pairs
list1 = [2, 4, 6]
list2 = [1, 3, 5]
result = tuple(i * j for i in list1 for j in list2)
print("Tuple 13.", result)