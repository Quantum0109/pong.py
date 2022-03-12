import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("windows 10")

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    all_sprites.update()
