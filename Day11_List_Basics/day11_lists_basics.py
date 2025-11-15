# 🐍 Python code for List Basics (Day 11)

# Creating a list
fruits = ["Apple", "Banana", "Orange"]
print("Full List:", fruits)

# Accessing elements
print("First item:", fruits[0])
print("Second item:", fruits[1])
print("Last item:", fruits[-1])

# Adding items
fruits.append("Grapes")
print("After append:", fruits)

# Updating items
fruits[1] = "Mango"
print("After update:", fruits)

# Slicing lists
print("Slice (0 to 2):", fruits[0:2])
print("Slice full list:", fruits[:])

# Length of list
print("Length:", len(fruits))
