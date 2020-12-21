class Game:
    def __init__(self):
        self.board = [' ' for _ in range(3)]  # range 3 x 3 default
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + '|'.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        # 0 | 1 | 2 tell us what number corresponds to what box
        for row in [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]:
            print('| ' + '|'.join(row) + ' |')

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, character):
        if self.board[square] == ' ':
            self.board[square] = character
            return True
        return False

    def available_moves(self):
        return [index for index, square in enumerate(self.board) if square == ' ']
        # moves = []
        # for (index, value) in enumerate(self.board):
        #     if value == ' ':
        #         moves.append(index)
        # return moves


