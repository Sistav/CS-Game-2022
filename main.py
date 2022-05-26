import pygame
from player import *

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

# Creates the players squares (Should attach to the player themselves)
rect1 = pygame.Rect(0, 0, 20, 20)
rect2 = pygame.Rect(0, 0, 20, 20)

# Creates the player
# Creates the players
player1 = Player([pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d],pygame.K_SPACE,[pygame.K_e,pygame.K_q],rect1,(255, 0, 0))
player2 = Player([pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT],pygame.K_SPACE,[pygame.K_e,pygame.K_q],rect2,(0, 0, 255))

# player2 = Player()

# Gameloop
run = True
while run:
    clock.tick(60)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Get a bool of every key pressed
    keys = pygame.key.get_pressed()
    
    # Check player movement (need to make this a for loop)
    for i in range(len(Player.players)):
        Player.players[i].check_movement(keys,window)


    window.fill(0)

    for i in range(len(Player.players)):
        Player.players[i].draw(window)
    
    # rect(window, (0, 0, 255), rect1)
    # pygame.draw.rect(window, (255, 0, 0), rect2)
    # pygame.draw.line(window, (100, 100, 255), (rect1.centerx, rect1.centery), (rect2.centerx, rect2.centery), 8) 


    pygame.display.flip()

pygame.quit()
exit()