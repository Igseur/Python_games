import pygame
import sys
from game import Game

pygame.init()

# fenetre principale + nom de la fenetre
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("new_game")

#image fond d'écran
background = pygame.image.load('fond.png')
game = Game()

#baniere pour la page de start
baniere = pygame.image.load('baniere.png')
baniere_rect = baniere.get_rect()

# boutton play
play_button = pygame.image.load('bouton_play.png')
play_button = pygame.transform.scale(play_button,(300,200))
play_button_rect = play_button.get_rect()
play_button_rect.x = 350
play_button_rect.y = 350


game_on = True

#boucle
while game_on:

    screen.blit(background, (-1,0))

    #vérifie si le jeu à commencer
    # ( si oui commencer lancer le jeu )
    if game.is_playing:
        game.update(screen)
    # (sinon affiche la baniere et le bouton play
    else:
        screen.blit(baniere,(355,200))
        screen.blit(play_button, play_button_rect)

    pygame.display.flip()


    for event in pygame.event.get():
        # vérifie la croix de la page est actionné si oui ferme la page
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_a:
                game.player.launch_bdf()

            elif event.key == pygame.K_z:
                game.player.launch_bdf_2()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # vérifie si clique de la  souris et que c'est sur la position du bouton play
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if play_button_rect.collidepoint(event.pos):
                # lancer le jeu
                game.start()