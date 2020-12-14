from rock_paper_scissors.classes.Player import Player
from rock_paper_scissors.classes.Game import Game


def start_game():
    name_1 = input("Enter name of player 1")
    name_2 = input("Enter name of player 2")

    player1 = Player(name_1)
    player2 = Player(name_2)

    game = Game(player1, player2)

    while not game.check_winner_game():
        print(f"Turn {game.turns}")
        game.turn()

    print(f"Winner {game.check_winner_game()} before {game.turns} turns")


start_game()
