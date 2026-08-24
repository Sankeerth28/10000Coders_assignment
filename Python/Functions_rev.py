def check_anagram(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())


def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)
    return unique_numbers[1]


def flatten_list(nested_list):
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


def is_armstrong(number):
    if number < 0:
        return False

    digits = str(number)
    sum_of_cubes = sum(int(digit) ** 3 for digit in digits)

    return sum_of_cubes == number


# Example usage
print(check_anagram("listen", "silent"))       # True
print(check_anagram("hello", "world"))         # False

print(second_largest([10, 5, 8, 10, 3]))       # 8
print(second_largest([5, 5, 5]))               # None

print(flatten_list([1, [2, 3], [4, [5, 6]]])) # [1, 2, 3, 4, 5, 6]

print(is_armstrong(371))                       # True
print(is_armstrong(123))                       # False