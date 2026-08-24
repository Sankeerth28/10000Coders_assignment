# Dictionary Comprehensions Practice

# 1. Create a new dictionary containing only keys with even values.
data1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result1 = {k: v for k, v in data1.items() if v % 2 == 0}

# 2. Double all values in the dictionary.
data2 = {'x': 1, 'y': 2, 'z': 3}
result2 = {k: v * 2 for k, v in data2.items()}

# 3. Create a dictionary with squares from 1 to 10 as keys and cubes as values.
result3 = {n ** 2: n ** 3 for n in range(1, 11)}

# 4. Filter out keys with values less than 5.
data4 = {'p': 1, 'q': 6, 'r': 3, 's': 8}
result4 = {k: v for k, v in data4.items() if v >= 5}

# 5. Swap the keys and values of the original dictionary.
data5 = {'name': 'John', 'age': 30}
result5 = {v: k for k, v in data5.items()}

# 6. Create a dictionary where each number is a key and its square is the value.
numbers = [1, 2, 3, 4, 5]
result6 = {n: n ** 2 for n in numbers}

# 7. Keep only keys with values greater than 15.
data7 = {'monday': 10, 'tuesday': 20, 'wednesday': 30}
result7 = {k: v for k, v in data7.items() if v > 15}

# 8. Create a dictionary with fruit names as keys and their lengths as values.
fruits = ['apple', 'banana', 'cherry']
result8 = {fruit: len(fruit) for fruit in fruits}

# 9. Add 10 to each value in the dictionary.
data9 = {'jan': 100, 'feb': 200, 'mar': 300}
result9 = {k: v + 10 for k, v in data9.items()}

# 10. Keep programming languages first released before 1995.
data10 = {'python': 1991, 'java': 1995, 'c++': 1983}
result10 = {k: v for k, v in data10.items() if v < 1995}
