import random

user_wins, computer_wins, draw = 0, 0, 0

print(f"Rock, Paper, Scissors")

options = ["rock", "paper", "scissors"]

while True:
    user_input = input(f"Choose Rock/Paper/Scissors or Choose Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Typo. Type again!")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"The computer picked '{computer_pick}'.")
    # rock:0 paper:1 scissors:2

    if user_input == "rock" and computer_pick == "scissors":
        print(f"You Win!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == computer_pick:
        print("Draw")
        draw += 1
        continue

    else:
        print("You Lost!")
        computer_wins += 1


print(f"\nYou win '{user_wins}' time(s).\n")
print(f"The Computer wins '{computer_wins}' time(s).\n")
print(f"Draws occurred '{draw}' time(s).\n\n")


if user_wins > computer_wins:
    print("Final Result: Yayyy! Congratulations.You Won")
elif user_wins < computer_wins:
    print("Final Result: OOOPPS! Computer scored more than you.")
else:
    print("Final Result: Its a DRAW.")


print("GoodBye!")
