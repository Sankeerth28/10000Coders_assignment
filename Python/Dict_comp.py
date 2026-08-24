# 1
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = {k: v for k, v in original.items() if v % 2 == 0}

# 2
original = {'x': 1, 'y': 2, 'z': 3}
result = {k: v * 2 for k, v in original.items()}

# 3
result = {n ** 2: n ** 3 for n in range(1, 11)}

# 4
original = {'p': 1, 'q': 6, 'r': 3, 's': 8}
result = {k: v for k, v in original.items() if v >= 5}

# 5
original = {'name': 'John', 'age': 30}
result = {v: k for k, v in original.items()}

# 6
numbers = [1, 2, 3, 4, 5]
result = {n: n ** 2 for n in numbers}

# 7
original = {'monday': 10, 'tuesday': 20, 'wednesday': 30}
result = {k: v for k, v in original.items() if v > 15}

# 8
fruits = ['apple', 'banana', 'cherry']
result = {fruit: len(fruit) for fruit in fruits}

# 9
original = {'jan': 100, 'feb': 200, 'mar': 300}
result = {k: v + 10 for k, v in original.items()}

# 10
original = {'python': 1991, 'java': 1995, 'c++': 1983}
result = {k: v for k, v in original.items() if v < 1995}