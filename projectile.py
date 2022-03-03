import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image= pygame.image.load('image/bdf.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

    def remove_bdf(self):
        self.player.all_bdf.remove(self)

    def move_bdf(self):
        self.rect.x -= self.velocity
        for monster in self.player.game.check_collision(self,self.player.game.all_monster):
            self.remove_bdf()
            monster.dammage(self.player.attack)

        if self.rect.x < -10:
            self.remove_bdf()