
class Score:
    def __init__(self):

        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        self.winner = None
        self.lines = self.make_lines()

    def make_lines(self):
        return [
            self.board[0],
            self.board[1],
            self.board[2],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]],
        ]

    def check_board(self, board):
        self.board = board
        self.lines = self.make_lines()
        for x in self.lines:
            if x == ["X", "X", "X"]:
                self.winner = "X WINS"
                return True
            elif x == ["O", "O", "O"]:
                self.winner = "O WINS"
                return True
        return False

    def add_piece(self, selected_square, drop_point):
        self.board[drop_point[0]][drop_point[1]] = selected_square.score_value



