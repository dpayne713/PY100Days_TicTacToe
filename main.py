import sys
import pygame
from piece import PieceX, PieceO
from board import Board
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        self.screen = pygame.display.set_mode(size=(400, 400))
        self.screen_rect = self.screen.get_rect()
        self.screen_rect_center = self.screen_rect.center
        self.board = Board(self)
        self.score = Score()
        self.current_piece = None
        self.turn = ""

        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render("Tic Tac Toe", True, 'Blue')
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom


        self.pieces = [PieceX(self), PieceO(self)]
        self.placed_pieces = []

        self.game_over = False

    def run_game(self):
        while True:
            self._events()
            self._movement()
            self._draw()

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                self.click_logic(click_pos)

    def click_logic(self, click_pos):
        if not self.game_over:

            for x in self.pieces:
                # x.clicked returns true if element is already clicked
                if x.clicked:
                    # x.drop returns dropped point only if it is available
                    drop_point = x.drop(self.score.board)
                    if drop_point:
                        self._scoring(x, drop_point)
                        if x.score_value == "X":
                            self.turn = "O"
                            self.pieces.append(PieceX(self))
                        else:
                            self.turn = "X"
                            self.pieces.append(PieceO(self))
                else:
                    if self.turn == "":
                        if x.rect.collidepoint(click_pos):
                            self.turn = x.score_value
                            x.pick_up(click_pos, self.turn)
                    elif self.turn == x.score_value:
                        x.pick_up(click_pos, self.turn)

    def _movement(self):
        for x in self.pieces:
            if x.clicked:
                x.drag_me(pygame.mouse.get_pos())


    def _scoring(self, selected_square, drop_point):

        self.score.add_piece(selected_square, drop_point)

        if self.score.check_board(self.score.board):
            self.text = self.font.render(self.score.winner, True, "Red")
            self.game_over = True




    def _draw(self):
        self.screen.fill(color=(0, 0, 0))
        self.screen.blit(self.text, self.text_rect)
        for x in self.placed_pieces:
            x.blitme()
        for x in self.pieces:
            x.blitme()
        self.board.blitme()
        pygame.display.flip()

game = Game()
game.run_game()

