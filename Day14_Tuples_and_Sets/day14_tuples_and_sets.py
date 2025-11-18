# 🐍 Python code for Tuples and Sets (Day 14)

# -----------------------------------
# 📘 Tuples (Ordered + Immutable)
# -----------------------------------

# Creating a tuple
numbers = (10, 20, 30, 40)
print("Tuple:", numbers)

# Accessing items
print("First item:", numbers[0])
print("Last item:", numbers[-1])

# Tuple unpacking
a, b, c, d = numbers
print("Unpacked values:", a, b, c, d)

# Tuple slicing
print("Slice (1:3):", numbers[1:3])

# Nested tuple
nested = (1, 2, (3, 4))
print("Nested tuple:", nested)
print("Access nested value:", nested[2][1])

# Count + Index
sample = (10, 20, 10, 30)
print("Count of 10:", sample.count(10))
print("Index of 30:", sample.index(30))

# -----------------------------------
# 📘 Sets (Unordered + Unique)
# -----------------------------------

# Creating a set
fruits = {"Apple", "Banana", "Orange", "Apple"}  # duplicate removed
print("\nSet:", fruits)

# Adding items
fruits.add("Grapes")
print("After add:", fruits)

# Removing items
fruits.remove("Orange")
print("After remove:", fruits)

# Membership check
print("Is 'Apple' in set?", "Apple" in fruits)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\nUnion:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))

# Updating sets
set1.update([10, 20])
print("After update:", set1)

# Removing duplicates using set
numbers_list = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers_list)
print("\nList with duplicates:", numbers_list)
print("Unique values using set:", unique_numbers)
