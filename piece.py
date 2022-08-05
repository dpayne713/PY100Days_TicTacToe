import pygame

class Piece:
    def __init__(self, game):

        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.board_pieces = game.board.squares
        self.score = game.score.board
        self.score_value = ""

        self.image = pygame.image.load("images/white_x.png")
        self.rect = self.image.get_rect()
        self.dropped_point = None
        self.clicked = False
        self.locked = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def pick_up(self, coord, turn):
        if self.locked:
            return
        # pick up piece
        if self.rect.collidepoint(coord):
            self.clicked = True
            return

    def drop(self, score_board):
        # Enumerate through board squares to check for collisions of piece
        for i, x in enumerate(self.board_pieces):
            # 2nd list layer
            for j, y in enumerate(x):
                if y.collidepoint(self.rect.center):
                    # Verify nothing is already at this position in score
                    if score_board[i][j] == "":
                        self.rect.center = y.center
                        self.clicked = False
                        self.locked = True
                        self.dropped_point = i, j
                        return i, j

    def drag_me(self, coord):
        # drag piece
        self.rect.center = pygame.mouse.get_pos()


class PieceX(Piece):
    def __init__(self, game):
        super().__init__(game)
        self.score_value = "X"
        self.rect.topright = self.screen_rect.topright
        self.rect.x -= 10
        self.rect.y += 10


class PieceO(Piece):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load("images/white_o.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft
        self.score_value = "O"
        self.rect.x += 10
        self.rect.y += 10

