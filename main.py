import pygame
from player import *


pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


# Creates the players
player1_movement = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
player2_movement = [pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT]


player1 = Player(player1_movement,pygame.K_SPACE,[pygame.K_e,pygame.K_q],(255, 0, 0))
player2 = Player(player2_movement,pygame.K_SPACE,[pygame.K_e,pygame.K_q],(0, 0, 255))


# Gameloop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # print(event.type)
    # Get a bool of every key pressed
    keys = pygame.key.get_pressed()
    
    # Check player movement (need to make this a for loop)
    for i in range(len(Player.players)):
        Player.players[i].check_movement(keys,window)

    # Make the background Black
    window.fill((0,0,0))

    # Draw out each player's sprite
    for i in range(len(Player.players)):
        Player.players[i].draw(window)
    
    # rect(window, (0, 0, 255), rect1)
    # pygame.draw.rect(window, (255, 0, 0), rect2)
    # pygame.draw.line(window, (100, 100, 255), (player1.sprite.centerx, player1.sprite.centery), (player2.sprite.centerx, player2.sprite.centery), 8) 

    # Render it
    pygame.display.flip()

pygame.quit()
exit()