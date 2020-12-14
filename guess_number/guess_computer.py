import random


def guess_computer(low, high):
    while True:
        try:
            guess = random.randint(low, high)
            feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)").upper()
            if feedback == 'H':
                high = guess - 1
            elif feedback == 'L':
                low = guess + 1
            elif feedback == 'C':
                print(f'Guessed {guess}')
                break
            else:
                print("Enter H / L / C please")
        except ValueError:
            print("If you want play more restart and don't fool me ")
            break


guess_computer(1, 5)  # Think a number between this two values
