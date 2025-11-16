# 🐍 Python code for List Methods (Day 12)

numbers = [10, 20, 30, 40]
print("Original list:", numbers)

# 1. append() → add at end
numbers.append(50)
print("After append:", numbers)

# 2. insert() → add at index
numbers.insert(1, 15)
print("After insert:", numbers)

# 3. remove() → remove by value
numbers.remove(30)
print("After remove:", numbers)

# 4. pop() → remove last item (or index)
numbers.pop()
print("After pop:", numbers)

# 5. sort() → ascending
numbers.sort()
print("Sorted ascending:", numbers)

# 6. reverse() → reverse list
numbers.reverse()
print("Reversed list:", numbers)

# 7. count() → count occurrences
print("Count of 20:", numbers.count(20))

# 8. index() → find index of value
print("Index of 15:", numbers.index(15))

# 9. extend() → add multiple items
numbers.extend([100, 200, 300])
print("After extend:", numbers)
