# 🐍 Python Code for Loops (Day 06)

# 🔁 1. For Loop
print("For Loop Example:")
for i in range(1, 6):
    print("Count:", i)

# 🔄 2. While Loop
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# 🧩 3. Looping through a list
fruits = ["🍎 Apple", "🍌 Banana", "🍇 Grapes"]
print("\nLooping through a list:")
for fruit in fruits:
    print(fruit)

# ⚡ 4. Using break and continue
print("\nBreak and Continue Example:")
for num in range(1, 6):
    if num == 3:
        continue  # Skip 3
    if num == 5:
        break     # Stop at 5
    print("Number:", num)
