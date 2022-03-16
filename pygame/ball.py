import pygame

"""
    screen,
    width,
    height,
    velocity_x,
    velocity_y,
    color,
    center_x,
    center_y
"""
class Ball:
    def __init__(self,
        screen,
        width=100,
        height=100,
        velocity_x=3,
        velocity_y=3,
        color=(255, 255, 255),
        centerx=400,
        centery=300,
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.Surface((10, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def draw(self):
        self.screen.blit(self.image, self.rect)
