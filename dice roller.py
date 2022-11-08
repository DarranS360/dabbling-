import random
dice_min = 1
dice_max = 6

roll = input("Would you like to roll a d6?\n")

while roll == "yes" or roll == "y":
    print("Rolling the dices...")
    print("The value is....")
    print(random.randint(dice_min, dice_max))
    roll_again = input("Roll the dices again?\n")
    if roll_again == "no" or roll_again == "n":
        break
print("Okay, no more dice to roll right now :-)")
