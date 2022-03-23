import pygame


pygame.font.init()
myfont = pygame.font.Font('assets/PressStart2P.ttf', 32)

class Score:
    def __init__(
        self,
        screen,
        color=(255, 255, 255),
        centerx=100,
        centery=50,
        owner=None,
        score=0
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = color
        self.owner = owner
        self.score = score
        self.image = myfont.render(str(self.score), False, self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery


    def draw(
        self
    ):
        self.screen.blit(self.image, self.rect)

    def update(
        self,
    ):
        self.image = myfont.render(str(self.score), False, self.color)
