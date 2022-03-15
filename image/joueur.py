import pygame
from projectile import Projectile
from projectile2 import Projectile2

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 10
        self.jump = 3
        self.game = game
        self.all_bdf = pygame.sprite.Group()
        self.all_bdf_2 = pygame.sprite.Group()
        self.image = pygame.image.load('player1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 45
        self.rect.y = 25


    def launch_bdf(self):
        #créer une nouvelle instance de la classe projectile
        bdf = Projectile(self)
        self.all_bdf.add(bdf)

    def launch_bdf_2(self):
        #créer une nouvelle instance de la classe projectile
        bdf2 = Projectile2(self)
        self.all_bdf_2.add(bdf2)

    def dammage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    #affiche la bar de point de vie
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (64, 62, 61), [self.rect.x - 10, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x - 10, self.rect.y -10, self.health, 5])





    # déplace le joueur vers la droite avec la vitesse attribué
    def move_right(self):
        self.rect.x += self.velocity

    # déplace le joueur vers la gauche avec la vitesse attribué
    def move_left(self):
        #vérifie si il n'a pas de collision avec un monstre pour le faire avancer vers la gauche
        if not self.game.check_collision(self,self.game.all_monster):
            self.rect.x -= self.velocity

    def move_up(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.y -= self.velocity

    def move_down(self):
        if not self.game.check_collision(self, self.game.all_monster) :
            self.rect.y += self.velocity

