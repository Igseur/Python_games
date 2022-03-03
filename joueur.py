import pygame
from projectile import Projectile
from pomme import Pomme

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.jump = 3
        self.game = game
        self.all_bdf = pygame.sprite.Group()
        self.image = pygame.image.load('image/player1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 360


    def launch_bdf(self):
        bdf = Projectile(self)
        self.all_bdf.add(bdf)


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
        if not self.game.check_collision(self,self.game.all_monster):
            self.rect.y -= self.velocity

    def move_down(self):
        if not self.game.check_collision(self,self.game.all_monster):
            self.rect.y += self.velocity

    def teleportation(self):
        if self.rect.y == 360:
            self.rect.x = 300
            self.rect.y = 160
        elif self.rect.y == 160 :
            self.rect.x = 400
            self.rect.y = 360

    def heal(self):
        if self.game.check_collision(self,self.game.all_pomme):
            self.health += self.pomme.heal
