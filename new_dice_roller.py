import random
rolling = True

while rolling:
    dice_type = input("What type of dice would you like to roll: \n").lower()
    dice_num = int(input(f"How many {dice_type}s would you like to roll? \n"))
    end = 0
    total = 0

    while end < dice_num:
        if dice_type == "d20":
            roll = int(random.randint(1, 20))
            total += roll

        elif dice_type == "d12":
            roll = int(random.randint(1, 12))
            total += roll

        elif dice_type == "d10":
            roll = int(random.randint(1, 10))
            total += roll

        elif dice_type == "d8":
            roll = int(random.randint(1, 8))
            total += roll

        elif dice_type == "d6":
            roll = int(random.randint(1, 6))
            total += roll

        elif dice_type == "d4":
            roll = int(random.randint(1, 4))
            total += roll

        end += 1
    print(f"Your result of rolling {dice_num} {dice_type} is: {total}!")

run = False
