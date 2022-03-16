"""
    Paddle(screen,
           width,
           height,
           color,
           centerx,
           centery,
           velocity
    )
"""

import pygame

class Player():
    def __init__(self,
           screen,
           width=10,
           height=100,
           color=(255, 255, 255),
           centerx=100,
           velocity=3,
           is_auto=False,
           key_up=pygame.K_UP,
           key_down=pygame.K_DOWN
    ):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.Surface((10, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = self.screen_rect.centery
        self.is_auto = is_auto
        self.key_up = key_up
        self.key_down = key_down
        self.velocity = velocity

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def control(self, keys):
        if self.is_auto == True:
            pass
        else:
            if keys[self.key_up]:
                self.rect.y -= self.velocity
            if keys[self.key_down]:
                self.rect.y += self.velocity 




