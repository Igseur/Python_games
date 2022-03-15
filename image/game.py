import pygame
from joueur import Player
from monstre import monster



class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.all_monster2 = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.all_monster2 = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        for bdf in self.player.all_bdf:
            bdf.move_bdf()

        for bdf2 in self.player.all_bdf_2:
            bdf2.move_bdf2()


        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)


        self.player.all_bdf.draw(screen)

        self.all_monster.draw(screen)


        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 890:
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 45:
            self.player.move_left()

        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 20:
            self.player.move_up()

        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 680:
            self.player.move_down()




    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)



    def spawn_monster(self):
        monstre = monster(self)
        self.all_monster.add(monstre)


