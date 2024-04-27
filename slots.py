import random

items = ["🍒", "🍇", "🍋", "7️⃣"]

result = random.choices(items, k = 3)

print("")

print(result[0], " | ", result[1], " | ", result[2])

if result[0] == result[1] == result[2]:
    
    print("\nYou Won!!")
else:
    
    print("\nYou Lost :( Try Again?\n")