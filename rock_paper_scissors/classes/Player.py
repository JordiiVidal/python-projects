class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0

    def winner(self):
        self.wins += 1
