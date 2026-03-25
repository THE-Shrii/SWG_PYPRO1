# =========================================================
# 🐍 SNAKE WATER GUN GAME (COMPLETE PROGRAM)
# =========================================================

import random

# 1 for Snake, -1 for Water, 0 for Gun
computer = random.choice([1, -1, 0])

youstr = input("Enter choice (s for Snake, w for Water, g for Gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print("You chose:", reverseDict[you])
print("Computer chose:", reverseDict[computer])


# =========================================================
# 📌 GAME LOGIC
# =========================================================

# Snake drinks Water → Snake wins
# Water damages Gun → Water wins
# Gun kills Snake → Gun wins

if computer == you:
    print("It's a Draw")

else:
    if (computer == -1 and you == 1):      # Snake vs Water
        print("You Win")
    elif (computer == 1 and you == -1):
        print("You Lose")

    elif (computer == 0 and you == -1):    # Gun vs Water
        print("You Win")
    elif (computer == -1 and you == 0):
        print("You Lose")

    elif (computer == 1 and you == 0):     # Snake vs Gun
        print("You Win")
    elif (computer == 0 and you == 1):
        print("You Lose")


# =========================================================
# 🎯 END OF GAME
# =========================================================










# =========================================================
# 🐍 OPTIMIZED SNAKE WATER GUN GAME
# =========================================================

import random

# Mapping
choices = {"s": 1, "w": -1, "g": 0}
reverse = {1: "Snake", -1: "Water", 0: "Gun"}

# Input
you = choices[input("Enter (s/w/g): ")]
computer = random.choice([1, -1, 0])

print("You:", reverse[you])
print("Computer:", reverse[computer])

# =========================================================
# 🔥 SIMPLE LOGIC USING MATH
# =========================================================

if you == computer:
    print("Draw")

elif (you - computer) == 1 or (you - computer) == -2:
    print("You Win")

else:
    print("You Lose")