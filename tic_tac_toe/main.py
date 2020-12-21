from tic_tac_toe.classes.Player import Player
from tic_tac_toe.classes.Game import Game


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()

    character = 'X'

    while game.empty_squares():
        if character == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        # replace character for Player instance
        if game.make_move(square, character):
            if print_game:
                print(f'{character} makes a move to square {square}')
                game.print_board()
                print(' ')

            character = 'O' if character == 'X' else 'X'
