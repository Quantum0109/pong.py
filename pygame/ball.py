"""
    очки на экране 2 штука
    class Score(screen, owner, color, width, height)
"""

import pygame



class Ball:
    def __init__(self,
        screen,
        width=20,
        height=20,
        velocity_x=1,
        velocity_y=1,
        color=(255, 255, 255),
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def draw(
        self
    ):
        self.screen.blit(self.image, self.rect)

    def movement(
        self,
        player,
        opponent
    ): 
        self.rect.x += self.velocity_x
        self.rect.y -= self.velocity_y
        if self.rect.top <= self.screen_rect.top:
            self.velocity_y *= -1
        elif self.rect.bottom >= self.screen_rect.bottom:
            self.velocity_y *= -1
        # TODO: нет колизий право и лево
        if self.rect.colliderect(player.rect) or self.rect.colliderect(opponent.rect):
            self.velocity_x *= -1
            self.velocity_y *= -1