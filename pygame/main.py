import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("windows 10")

all_sprites = pygame.sprite.Group()
player = Player(screen)
all_sprites.add(player)

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
                    
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(400)
