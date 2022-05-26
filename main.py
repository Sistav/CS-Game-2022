import pygame
from player import *
from bullet import *

pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


# Creates the players
player1_movement = [pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]
player2_movement = [pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT]


player1 = Player(player1_movement,pygame.K_SPACE,[pygame.K_e,pygame.K_q],(255, 0, 0))
player2 = Player(player2_movement,pygame.K_SLASH,[pygame.K_COMMA,pygame.K_PERIOD],(0, 0, 255))


# Gameloop
run = True

# How many ticks per second
tickrate = 60

# Please keep this at 0, this is used for bullet lifetime counts
clock_cycle = 0


while run:
    # Tick and add to cycle count
    clock.tick(tickrate)
    clock_cycle += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get a bool of every key pressed
    keys = pygame.key.get_pressed()
    
    # Check player movement and if a bullet was shot
    for i in range(len(Player.players)):
        Player.players[i].check_movement(keys,window)
        Player.players[i].check_shot(keys,clock_cycle)
    
    
    bullet_index = 0
    while bullet_index < len(Bullet.bullets):
        # If the bullet has expired past it's lifetime...
        if (Bullet.bullets[bullet_index].spawn_tick + Bullet.bullets[bullet_index].lifetime) < clock_cycle:
            # Kill it
            del Bullet.bullets[bullet_index]
        else:
            # otherwise have it move accordingly and move onto the next bullet
            Bullet.bullets[bullet_index].move(window)
            bullet_index += 1 

        
    # Make the background Black
    window.fill((0,0,0))

    # Draw out each player's sprite 
    for i in range(len(Player.players)):
        Player.players[i].draw(window)
    
    # Draw out the bullets
    for i in range(len(Bullet.bullets)):
        Bullet.bullets[i].draw(window)
       

    # Render it
    pygame.display.flip()

pygame.quit()
exit()