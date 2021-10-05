import random

def guess(x):
    random_number= random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry,guess again. Your guess seems too low!")
        elif guess > random_number:
            print("Sorry,guess again. Your guess seems too high!")
            
    print(f"Yayy!! You guessed {random_number} correctly")


guess(17)