import pygame
import sys
from game import Game

pygame.init()

# fenetre principale + nom de la fenetre
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("image/gamelunch")

#image fond d'écran
background = pygame.image.load('image/fond_jeu.png')
game = Game()

#baniere pour la page de start
baniere = pygame.image.load('image/baniere.png')
baniere_rect = baniere.get_rect()

# boutton play
play_button = pygame.image.load('image/bouton_play.png')
play_button = pygame.transform.scale(play_button,(300,200))
play_button_rect = play_button.get_rect()
play_button_rect.x = 190
play_button_rect.y = 250

#plateforme
plateforme = pygame.image.load('image/plateforme.png')

game_on = True

#boucle
while game_on:

    screen.blit(background, (-1,0))

    #vérifie si le jeu à commencer
    # ( si oui commencer lancer le jeu )
    if game.is_playing:
        game.update(screen)
        screen.blit(plateforme,(200,150))
    # (sinon affiche la baniere et le bouton play
    else:
        screen.blit(baniere,(200,100))
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

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # vérifie si clique de la  souris et que c'est sur la position du bouton play
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if play_button_rect.collidepoint(event.pos):
                # lancer le jeu
                game.start()
