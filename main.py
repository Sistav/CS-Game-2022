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

scene_manager = Scene(0)

# Sets up the music and sets the volume to zero
song = "music_loop.wav"

# Begins the mixer and loads the song
pygame.mixer.init()
pygame.mixer.music.load(song)

# Sets the song to repeat
pygame.mixer.music.play(loops=-1)

# Minimize the volume so the intro can play
pygame.mixer.music.set_volume(0)

# Gameloop
run = True
while run:

    # Keeps an int of how long since the game was booted.
    # This will eventually break the code in 4,874,520,144.63 years, so if you think that needs a check, I hope you have time, to wait for it to error out.
    clock_cycle += 1
    clock.tick(tickrate)
    
    # Basic pygame window handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Start the first scene up
    scene_manager.clock_cycle = clock_cycle
    scene_manager.run()
    
    # refresh screen
    pygame.display.flip()

pygame.quit()
exit()