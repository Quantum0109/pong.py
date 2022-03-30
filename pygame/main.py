import pygame
from player import Player
from ball import Ball
from score import Score

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h
pygame.display.set_caption("windows 10")

all_sprites = pygame.sprite.Group()
player = Player(screen, centerx=WIDTH*0.05)
opponent = Player(screen, centerx=WIDTH*0.95, is_auto=True)
ball = Ball(screen)
player_score = Score(screen, owner=player, centerx=WIDTH*0.4)
opponent_score = Score(screen, owner=opponent, centerx=WIDTH*0.6)

clock = pygame.time.Clock()

game = True

while game:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        game = False
                    
    player.draw()
    player.control(keys, ball)
    opponent.control(keys, ball)
    opponent.draw()
    ball.draw()
    ball.goal(player_score, opponent_score, player, opponent)
    player_score.draw()
    opponent_score.draw()
    ball.movement(player, opponent)
    player_score.update()
    opponent_score.update()
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()