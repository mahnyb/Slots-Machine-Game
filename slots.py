import random
import os

items = ["🍒", "🍇", "🍋", "7️⃣"]

initial_balance = 100

while initial_balance > 0:
    print("---------------------------------------------------------")
    print(f"\nCurrent Balance: {initial_balance}\n")
    print("---------------------------------------------------------")
    
    input("\nPress Enter to play...")
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("---------------------------------------------------------")
    
    result = random.choices(items, k = 3)

    print("")

    print(result[0], " | ", result[1], " | ", result[2])

    if result[0] == result[1] == result[2]:
        initial_balance += 10
        print("\nYou Won!! +10 added to your balance\n")
    
    
    else:
        initial_balance -= 20
        print("\nYou Lost :( -20 deducted from your balance\n")
    
    print(f"\nCurrent Balance: {initial_balance}\n") # current balance after each round
    
    if initial_balance <0:
        print("\nGame Over. Your balance is zero\n")
    
    print("---------------------------------------------------------")
    
    choice = input("Do you want to continue playing (c) or withdraw (w)? ").lower()

    while choice not in ("c", "w"):
        print("Invalid choice. Please enter C for to continue playing or W to withdraw from the game")
    
    if choice == "w":
        print("You chose to withdraw. Game Over\n")
        break
    elif choice == "c":
        continue

print("---------------------------------------------------------")
print(f"Final Balance: {initial_balance}\n")
print("Thanks for playing :3")
