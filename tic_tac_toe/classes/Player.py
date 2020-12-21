import math
import random


class Player:
    # X or 0 (character)
    def __init__(self, character):
        self.character = character

    def get_move(self, game):
        pass


class ComputerPlayer(Player):

    def __init__(self, character):
        super().__init__(character)

    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):

    def __init__(self, character):
        super().__init__(character)

    def get_move(self, game):
        valid_value = False
        val = None
        print(f'Turn of {self.character}, available moves {game.available_moves()}')
        while not valid_value:
            try:
                val = int(input('Choose one of them : '))
                if val not in game.available_moves:
                    raise ValueError
                valid_value = True
            except ValueError:
                print("Invalid Option")
        return val




