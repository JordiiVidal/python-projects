import random


def play():

    user = input('Rock (R) / Paper (P) / Scissors (S)').upper()
    computer = random.choice(['R', 'P', 'S'])
    print(f" User : {user} VS Computer : {computer}")

    if user == computer:
        return "Draw"
    else:
        if winner(user, computer):
            return "Winner User"

        return "Winner Computer"


def winner(player1, player2):
    if (player1 == 'R' and player2 == 'S')\
            or (player1 == 'S' and player2 == 'P')\
            or (player1 == 'P' and player2 == 'R'):
        return True
    else:
        return False


play()
