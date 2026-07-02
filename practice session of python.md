# ASSIGNMENT

**Date:** 25-06-2026
**Tech Stack:** Python
**Topic:** Python Data Types

---

## 1. What is an Integer (int) in Python? Write its features with an example.

**Answer:**

An **Integer (int)** is a data type used to store whole numbers without decimal values. It can be positive, negative, or zero.

**Features:**

* Stores whole numbers.
* Immutable (cannot be changed).
* Supports arithmetic operations.
* Can store positive, negative, and zero values.

**Example:**

```python
age = 21
print(age)
print(type(age))
```

---

## 2. What is a String (str) in Python? Write its features with an example.

**Answer:**

A **String (str)** is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes.

**Features:**

* Used to store text.
* Immutable.
* Supports indexing and slicing.
* Allows duplicate characters.
* Maintains insertion order.

**Example:**

```python
name = "Lucky"
print(name)
print(type(name))
```

---

## 3. What is a List (list) in Python? Write its features with an example.

**Answer:**

A **List** is an ordered collection of items enclosed in square brackets (`[]`).

**Features:**

* Mutable (can be modified).
* Allows duplicate values.
* Maintains insertion order.
* Supports indexing and slicing.
* Can store different data types.

**Example:**

```python
numbers = [10, 20, 30, 20]
print(numbers)
print(type(numbers))
```

---

## 4. What is a Tuple (tuple) in Python? Write its features with an example.

**Answer:**

A **Tuple** is an ordered collection of items enclosed in parentheses (`()`).

**Features:**

* Immutable.
* Allows duplicate values.
* Maintains insertion order.
* Supports indexing and slicing.

**Example:**

```python
colors = ("Red", "Blue", "Green")
print(colors)
print(type(colors))
```

---

## 5. What is a Set (set) in Python? Write its features with an example.

**Answer:**

A **Set** is an unordered collection of unique elements enclosed in curly braces (`{}`).

**Features:**

* Mutable.
* Does not allow duplicate values.
* Does not support indexing or slicing.
* Used to store unique elements.

**Example:**

```python
fruits = {"Apple", "Banana", "Mango"}
print(fruits)
print(type(fruits))
```

---

## 6. What is a Dictionary (dict) in Python? Write its features with an example.

**Answer:**

A **Dictionary** stores data in the form of **key-value pairs**.

**Features:**

* Mutable.
* Keys must be unique.
* Values can be duplicated.
* Maintains insertion order.
* Values are accessed using keys.

**Example:**

```python
student = {
    "name": "Lucky",
    "age": 21
}

print(student)
print(type(student))
```

---

## 7. Which Python data types are mutable and which are immutable?

**Mutable Data Types**

* List
* Set
* Dictionary

**Immutable Data Types**

* Integer
* Float
* Boolean
* String
* Tuple

---

## 8. Which data types allow duplicate values?

**Allow duplicates:**

* String
* List
* Tuple
* Dictionary values

**Do not allow duplicates:**

* Set
* Dictionary keys

---

## 9. Which data types maintain the insertion order?

The following data types maintain insertion order:

* String
* List
* Tuple
* Dictionary

**Note:** Set does not guarantee insertion order.

---

## 10. Which data types support indexing and slicing?

The following data types support both indexing and slicing:

* String
* List
* Tuple

Dictionary uses keys to access values, while Set does not support indexing or slicing.

---

## 11. Write one example for each data type and print its type using the `type()` function.

```python
a = 100
print(type(a))

b = "Python"
print(type(b))

c = [1, 2, 3]
print(type(c))

d = (10, 20, 30)
print(type(d))

e = {5, 10, 15}
print(type(e))

f = {"name": "Lucky", "age": 21}
print(type(f))
```

**Output:**

```
<class 'int'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
```

---

## 12. Comparison Table

| Feature                   | int  | str       | list      | tuple     | set       | dict        |
| ------------------------- | ---- | --------- | --------- | --------- | --------- | ----------- |
| Stores Single Value       | Yes  | No        | No        | No        | No        | No          |
| Mutable                   | No   | No        | Yes       | No        | Yes       | Yes         |
| Immutable                 | Yes  | Yes       | No        | Yes       | No        | No          |
| Allows Duplicates         | No   | Yes       | Yes       | Yes       | No        | Values: Yes |
| Ordered                   | Yes  | Yes       | Yes       | Yes       | No        | Yes         |
| Supports Indexing         | No   | Yes       | Yes       | Yes       | No        | No          |
| Supports Slicing          | No   | Yes       | Yes       | Yes       | No        | No          |
| Can Store Multiple Values | No   | Yes       | Yes       | Yes       | Yes       | Yes         |
| Example                   | `10` | `"Hello"` | `[1,2,3]` | `(1,2,3)` | `{1,2,3}` | `{"a":1}`   |

### Conclusion

Python provides different data types to store and organize data efficiently. Primitive data types like **int** and **str** store single values, while non-primitive data types such as **list**, **tuple**, **set**, and **dict** store collections of data. Understanding their features helps in choosing the appropriate data type for different programming tasks.
