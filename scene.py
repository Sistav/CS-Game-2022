import pygame
from bullet import *
from player import *
from wall import * 

class Scene:
    def __init__(self,start_type):
        self.window = pygame.display.set_mode((800, 800))

        self.background_color = (0,0,0)
        self.text_color = (255,255,255)

        self.fontsize = 32 
        
        
        self.mode = start_type
        
        spawnpoints = Wall.generate(self.window.get_width(),self.window.get_height())

        for i in range(len(Player.players)):
            choice = random.randint(0,len(spawnpoints)-1)
            spawn = spawnpoints[choice]
            del spawnpoints[choice]
            Player.players[i].x = spawn[0]
            Player.players[i].y = spawn[1]
            Player.players[i].angle = random.randint(0,360)


    def titlescreen(self):
        titlescreen = pygame.image.load('titlescreen.png')
        rect = titlescreen.get_rect()
        rect.center = self.window.get_width() // 2, self.window.get_height() // 2
        self.window.blit(titlescreen,rect)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] > 224 and pygame.mouse.get_pos()[0] < 591) and (pygame.mouse.get_pos()[1] > 448 and pygame.mouse.get_pos()[1] < 639):
                self.mode = 1
            else:
                self.titlescreen()
        
                    

    def gameplay(self):
        pygame.mixer.music.set_volume(1)
        
        font = pygame.font.Font('freesansbold.ttf', self.fontsize)
        
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Score', True, self.text_color, self.background_color)
        
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        
        # set the center of the rectangular object.
        textRect.center = (self.window.get_width()//2,self.fontsize)

        # Get a bool of every key pressed
        keys = pygame.key.get_pressed()
        
        # Check player movement and if a bullet was shot
        for i in range(len(Player.players)):
            old_player_x = Player.players[i].x
            old_player_y = Player.players[i].y
            Player.players[i].check_movement(keys,self.window)
            if Player.players[i].check_wall_collision():
                Player.players[i].x = old_player_x
                Player.players[i].y = old_player_y
    
            Player.players[i].check_shot(keys,self.clock_cycle)
            Player.players[i].check_bullet_colliosion()
        

        bullet_index = 0
        while bullet_index < len(Bullet.bullets):
            # If the bullet has expired past it's lifetime...
            if (Bullet.bullets[bullet_index].spawn_tick + Bullet.bullets[bullet_index].lifetime) < self.clock_cycle:
                # Kill it
                del Bullet.bullets[bullet_index]
            else:
               
                Bullet.bullets[bullet_index].move(self.window)
                Bullet.bullets[bullet_index].two_turns_ago_x = Bullet.bullets[bullet_index].one_turn_ago_x
                Bullet.bullets[bullet_index].two_turns_ago_y = Bullet.bullets[bullet_index].one_turn_ago_y
                Bullet.bullets[bullet_index].one_turn_ago_x = Bullet.bullets[bullet_index].x 
                Bullet.bullets[bullet_index].one_turn_ago_y = Bullet.bullets[bullet_index].y

                collided_wall = Bullet.bullets[bullet_index].check_wall_collision()
    
                if collided_wall != None:
                    Bullet.bullets[bullet_index].x =  Bullet.bullets[bullet_index].two_turns_ago_x
                    Bullet.bullets[bullet_index].y =  Bullet.bullets[bullet_index].two_turns_ago_y
                    bounce_type = Bullet.bullets[bullet_index].check_wall_collision_type(collided_wall)
                    if (bounce_type == 0):
                        Bullet.bullets[bullet_index].angle = 180 - Bullet.bullets[bullet_index].angle
                    elif (bounce_type == 1):
                        Bullet.bullets[bullet_index].angle = -Bullet.bullets[bullet_index].angle
                else:
                    bullet_index += 1 

            
        # Make the background Black
        self.window.fill(self.background_color)

        Wall.delete(self.clock_cycle)
        
        for i in range(len(Wall.walls)):
            Wall.walls[i].draw(self.window)

        # Draw out each player's sprite 
        for i in range(len(Player.players)):
            Player.players[i].draw(self.window)
        
        # Draw out the bullets
        for i in range(len(Bullet.bullets)):
            Bullet.bullets[i].draw(self.window)

        
        

        self.window.blit(text, textRect)

    def run(self):
        scenes = [self.titlescreen,self.gameplay]
        
        scenes[self.mode]()
