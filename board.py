import pygame

class Board:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect

        self.image = pygame.image.load('images/board_white.png')
        self.rect = self.image.get_rect()
        self.rect.center = game.screen_rect_center

        self.top_row = [
            pygame.Rect(50, 50, 98, 98),
            pygame.Rect(153, 50, 98, 98),
            pygame.Rect(255, 50, 98, 98)
        ]
        self.mid_row = [
            pygame.Rect(50, 150, 98, 98),
            pygame.Rect(153, 150, 98, 98),
            pygame.Rect(255, 150, 98, 98)
        ]
        self.btm_row = [
            pygame.Rect(50, 250, 98, 98),
            pygame.Rect(153, 250, 98, 98),
            pygame.Rect(255, 250, 98, 98)
        ]

        self.squares = [self.top_row,
                        self.mid_row,
                        self.btm_row]

    def blitme(self):
        self.screen.blit(self.image, self.rect)
