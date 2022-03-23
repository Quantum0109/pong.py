import pygame
from player import Player
from ball import Ball
from score import Score

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("windows 10")

all_sprites = pygame.sprite.Group()
player = Player(screen, centerx=100)
opponent = Player(screen, centerx=700, is_auto=True)
ball = Ball(screen)
player_score = Score(screen, owner=player, centerx=300)
opponent_score = Score(screen, owner=opponent, centerx=500)

pygame.mixer.music.load('Beethoven.ogg')
pygame.mixer.music.play()

sound1 = pygame.mixer.Sound('assets/1.wav')


clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:             
            if event.key == pygame.K_DOWN:    
                player.rect.y += 10
            elif event.key == pygame.K_UP:
                player.rect.y -= 10

    keys = pygame.key.get_pressed()
                    
    player.draw()
    player.control(keys, ball)
    opponent.control(keys, ball)
    opponent.draw()
    ball.draw()
    ball.goal(player_score, opponent_score)
    player_score.draw()
    opponent_score.draw()
    ball.movement(player, opponent)
    player_score.update()
    opponent_score.update()
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(400)

pygame.quit()