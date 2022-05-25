import pygame
from player import *

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

rect1 = pygame.Rect(0, 0, 20, 20)

rect2 = pygame.Rect(0, 0, 20, 20)

player1 = Player(pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d)
player2 = Player(pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    keys = pygame.key.get_pressed()
    
    
    player1.check_movement(keys)
    player2.check_movement(keys)

    rect1.x = player1.x
    rect1.y = player1.y
        
    rect1.centerx = rect1.centerx % window.get_width()
    rect1.centery = rect1.centery % window.get_height()

    rect2.x = player2.x
    rect2.y = player2.y
        
    rect2.centerx = rect2.centerx % window.get_width()
    rect2.centery = rect2.centery % window.get_height()

    window.fill(0)
    
    pygame.draw.rect(window, (0, 0, 255), rect1)
    pygame.draw.rect(window, (255, 0, 0), rect2)

    pygame.display.flip()

pygame.quit()
exit()