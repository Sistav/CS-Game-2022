import pygame
from player import *
from scene import *
from wall import *

pygame.init()
pygame.display.set_caption('Tank Game')
clock = pygame.time.Clock()


# Creates the players
player1_movement = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
player2_movement = [pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT]

player1 = Player(player1_movement,pygame.K_SPACE,[pygame.K_e,pygame.K_q],(255, 0, 0))
player2 = Player(player2_movement,pygame.K_SLASH,[pygame.K_COMMA,pygame.K_PERIOD],(0, 0, 255))


# How many ticks per second
tickrate = 60
# Please keep this at 0, this is used for bullet lifetime counts
clock_cycle = 0

scene_manager = Scene(1)

run = True
while run:

    clock_cycle += 1
    clock.tick(tickrate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    scene_manager.clock_cycle = clock_cycle
    scene_manager.run()
    
    pygame.display.flip()

pygame.quit()
exit()