print("THINK BEYOND THE BOX, THE QUESRIONS BEYOND MAY BE TRICKIER THAN THEY LOOK AND ONLY THOSE WITH THE SHARPEST OF MINDS WILL PASS THROUGH")


print("Welcome to TreasureIsland.")
print("Your Mission is to find the treasure.")

# First choice
choice_one = input("You at a crossroad. Where do you want to go? Type 'left' or 'right': ")
if choice_one.lower() == "left":
    # Second choice
    choice_two = input("You have reached a river. Do you want to 'swim' or 'wait'?: ")
    if choice_two.lower() == "wait":
        # Third choice
        choice_three = input("You are before three doors. Which door do you choose? Type 'red' 'yellow' or 'blue': ")
        if choice_three.lower() == "blue":
            print("You Win! You found the treasure!")
        elif choice_three.lower() == "red":
            print("You were burned by fire.")
            print("Game over.")
        elif choice_three.lower() == "yellow":
            print("You were eaten by beasts.")
            print("Game over.")
        else:
            print("You choose the wrong door")
            print("Game over")
    else:
        print("You were attacked by trout.")
        print("Game over.")
else:
    print("You fell into a hole.")
    print("Game over.")
