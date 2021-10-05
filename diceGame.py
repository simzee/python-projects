import random


def dice_roll(roll):
    while roll == "y".lower() or roll == "yes".lower():
        print("Rolling the dice")
        print(random.randint(1, 6))
        roll = input(f"Do You want to roll again?:\n")

        if roll == "n".lower() or roll == "no".lower():
            print("Thank You for playing!")
            break


roll = input("Lets Start? (yes/no): ")
dice_roll(roll)