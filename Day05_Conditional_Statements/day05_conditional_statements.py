# 🐍 Python Code for Conditional Statements (Day 05)

# 🧠 Example 1: Basic if-else
age = 18

if age >= 18:
    print("✅ You are eligible to vote!")
else:
    print("❌ You are not eligible to vote yet.")

# 🧩 Example 2: if - elif - else ladder
score = 85

if score >= 90:
    print("🏆 Grade: A+")
elif score >= 75:
    print("🎯 Grade: B")
elif score >= 60:
    print("👍 Grade: C")
else:
    print("⚠️ Grade: Needs Improvement")

# 🔄 Example 3: Nested if
is_logged_in = True
has_subscription = False

if is_logged_in:
    if has_subscription:
        print("🎬 Access granted! Enjoy your premium content.")
    else:
        print("🔒 Please upgrade to premium to watch this video.")
else:
    print("👤 Please log in to continue.")

# ⚡ Example 4: Ternary (Short if-else)
time = 20
message = "🌞 Good Day!" if time < 18 else "🌙 Good Evening!"
print(message)
