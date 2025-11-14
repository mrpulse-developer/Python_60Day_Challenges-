# 🐍 Python Code for String Methods (Day 09)

text = "  Hello Python World!  "

# 1. Length of string
print("Length:", len(text))

# 2. Changing case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())

# 3. Removing extra spaces
print("Strip:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())

# 4. Searching inside the string
print("Find 'Python':", text.find("Python"))
print("Starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with '!':", text.strip().endswith("!"))

# 5. Replace text
print("Replace Python -> World:", text.replace("Python", "World"))

# 6. Splitting and joining
words = text.strip().split(" ")
print("Split:", words)
print("Join with '-':", "-".join(words))

# 7. Accessing characters
cleaned = text.strip()
print("First character:", cleaned[0])
print("Last character:", cleaned[-1])
