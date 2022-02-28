import pygame
import random

class Pomme(pygame.sprite.Sprite):

    def __init__(self, player):
        self.heal = 40
        self.player = player
        self.image = pygame.image.load('pomme_heal.png')
        self.rect = self.image.get_rect()
        self.rect.x = 285 + random.randint(0,50)
        self.rect.y = 220


