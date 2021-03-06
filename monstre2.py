import pygame
import random
class monster2(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 2
        self.attack = 0.1
        self.image = pygame.image.load('monstre.png')
        self.rect = self.image.get_rect()
        self.rect.x = 10 + random.randint(300,950)
        self.rect.y = 10 + random.randint(-100, 300)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (64, 62, 61), [self.rect.x - 10, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x - 10, self.rect.y -10, self.health, 5])

    def dammage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 10 + random.randint(300,950)
            self.rect.y = 10 + random.randint(-100, 300)
            self.health = 100


    def remove_monster(self):
        self.player.all_monster.remove(self)


    def forward(self):
        if not self.game.check_collision(self,self.game.all_player):
            if self.rect.y < 600:
                self.rect.x -= self.velocity

            else:
                self.rect.x = 10 + random.randint(300,950)
                self.rect.y = 10 + random.randint(-100, 300)
                self.health = self.max_health

        else:
            self.game.player.dammage(self.attack)
