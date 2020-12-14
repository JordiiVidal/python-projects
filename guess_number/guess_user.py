import random


def guess(n):

    random_number = random.randint(0, n)
    while True:
        input_number = int(input(f"Guess a number between 0-{n} : "))
        if input_number > random_number:
            print("Too high, try again")
        elif input_number < random_number:
            print("Too low, try again")
        else:
            print("You win")
            break


guess(12)
