import pygame
import random
from degrees_to_velocity import *
# https://sfbgames.itch.io/chiptone сайт с музыкой

class Ball:
    def __init__(self,
        screen,
        width=20,
        height=20,
        velocity_x=10,
        velocity_y=10,
        speed=10,
        color=(255, 255, 255),
        delay=1000
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
        self.speed = speed
        self.delay = delay

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
        if self.rect.bottom >= self.screen_rect.bottom:
            self.velocity_y *= -1
        if self.rect.colliderect(player.rect) or self.rect.colliderect(opponent.rect):
            self.velocity_x *= -1
            self.velocity_y *= -1

    def ball_to_center(self, player_score, opponent_score):
        now = pygame.time.delay(self.delay)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        angle = random.randrange(67, 133)
        velocity = degrees_to_velocity(angle, self.speed)
        self.velocity_x = velocity[0] * random.choice((-1, 1))
        self.velocity_y = velocity[1]
        pygame.time.delay(self.delay)

    def goal(self, player_score, opponent_score, player, opponent):
        if self.rect.left <= self.screen_rect.left:
            opponent_score.score += 1
            self.ball_to_center(player, opponent)
        if self.rect.right >= self.screen_rect.right:
            player_score.score += 1
            self.ball_to_center(player, opponent)
