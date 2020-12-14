class Game:

    turns = 0
    player_winner_wins = 3

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def check_winner_game(self):
        if self.player1.wins == self.player_winner_wins:
            return self.player1.name
        elif self.player2.wins == self.player_winner_wins:
            return self.player2.name
        else:
            return False

    def turn(self):

        player1_turn = input(f"{self.player1.name} R / P / S ??")
        player2_turn = input(f"{self.player2.name} R / P / S ??")

        if player2_turn != player1_turn:
            if (player1_turn == 'R' and player2_turn == 'S') \
                    or (player1_turn == 'S' and player2_turn == 'P') \
                    or (player1_turn == 'P' and player2_turn == 'R'):
                self.player1.winner()
            else:
                self.player2.winner()

        self.turns += 1
        return True
