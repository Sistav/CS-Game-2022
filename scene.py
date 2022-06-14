import pygame
from bullet import *
from player import *
from wall import * 

class Scene:
    def __init__(self,start_type):
        self.width = 1280
        self.height = 720

        self.window = pygame.display.set_mode((self.width,self.height))

        self.mode = start_type
        self.last_mode = None
        
        self.animation_delay =  2

        self.max_frames = 69

    def titlescreen(self,first_time = False):
        if first_time:
            self.current_frame = 1
            self.start_time = self.clock_cycle
        
        photo = f"Frames\{self.current_frame}.png"
        frame = pygame.image.load(photo)

        frame_rect = frame.get_rect()
        frame_rect.center = self.window.get_width() // 2, self.window.get_height() // 2

        self.window.blit(frame,frame_rect)

        pygame.draw.rect(self.window, 'BLACK', frame_rect, 1)
        pygame.display.update()
        
        if ((self.start_time + self.animation_delay) < self.clock_cycle):  
            if self.current_frame < self.max_frames:
                self.current_frame += 1
                self.start_time = self.clock_cycle
        
        exit_left_x = 448
        exit_top_y = 528
        exit_right_x = 815
        exit_bottom_y = 687

        play_left_x = 448
        play_top_y = 288
        play_right_x = 815
        play_bottom_y = 447

        if pygame.mouse.get_pressed()[0] and self.current_frame == self.max_frames:
            mouse_location = pygame.mouse.get_pos()
            if (mouse_location[0] > play_left_x and mouse_location[0] < play_right_x) and (mouse_location[1] > play_top_y and mouse_location[1] < play_bottom_y):
                self.mode = 1
            elif (mouse_location[0] > exit_left_x and mouse_location[0] < exit_right_x) and (mouse_location[1] > exit_top_y and mouse_location[1] < exit_bottom_y):
                pygame.quit()
                exit()
             
                    
    def gameplay(self,first_time = False):
        if first_time:
            
            self.background_color = (0,0,0)

            # Turn up the music
            pygame.mixer.music.set_volume(1)
            
            # Set the font

            spawnpoints = Wall.generate(self.window.get_width(),self.window.get_height())

            for i in range(len(Player.players)):
                choice = random.randint(0,len(spawnpoints)-1)
                spawn = spawnpoints[choice]
                del spawnpoints[choice]
                Player.players[i].x = spawn[0]
                Player.players[i].y = spawn[1]
                Player.players[i].angle = random.randint(0,360)
        

            self.text_color = (255,255,255)

            self.fontsize = 32 

            self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)

        # create a text surface object,
        # on which text is drawn on it.
        text = self.font.render('Score', True, self.text_color, self.background_color)
        
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        
        # set the center of the rectangular object.
        textRect.center = (self.window.get_width()//2,self.fontsize)

        # Get a bool of every key pressed
        keys = pygame.key.get_pressed()
        
        # Check player movement and if a bullet was shot
        for i in range(len(Player.players)):
            # Set the last known safe position for the player to be in
            old_player_x = Player.players[i].x
            old_player_y = Player.players[i].y

            # Let the player move
            Player.players[i].check_movement(keys,self.window)

            # If the player was stupid enough to hit a wall
            if Player.players[i].check_wall_collision():
                # Send them back to the old co-ord
                Player.players[i].x = old_player_x
                Player.players[i].y = old_player_y

            # Check if the player shot
            Player.players[i].check_shot(keys,self.clock_cycle)

            # Check if the player was hit
            Player.players[i].check_bullet_collision()
        

        bullet_index = 0
        while bullet_index < len(Bullet.bullets):
            # If the bullet has expired past it's lifetime...
            if (Bullet.bullets[bullet_index].spawn_tick + Bullet.bullets[bullet_index].lifetime) < self.clock_cycle:
                # Kill it
                del Bullet.bullets[bullet_index]
            else:
                # Move the bullet   
                Bullet.bullets[bullet_index].move(self.window)
                
                # Set the previous two co-ords  
                Bullet.bullets[bullet_index].two_turns_ago_x = Bullet.bullets[bullet_index].one_turn_ago_x
                Bullet.bullets[bullet_index].two_turns_ago_y = Bullet.bullets[bullet_index].one_turn_ago_y

                Bullet.bullets[bullet_index].one_turn_ago_x = Bullet.bullets[bullet_index].x 
                Bullet.bullets[bullet_index].one_turn_ago_y = Bullet.bullets[bullet_index].y

                # Check if a bullet collided with a wall
                collided_wall = Bullet.bullets[bullet_index].check_wall_collision()
    
                # if the bullet hit a wall
                if collided_wall != None:
                    # Move the bullet back so it doesn't clip into the wall
                    Bullet.bullets[bullet_index].x =  Bullet.bullets[bullet_index].two_turns_ago_x
                    Bullet.bullets[bullet_index].y =  Bullet.bullets[bullet_index].two_turns_ago_y

                    # Figure out whether to bounce the bullet on the x or the y axis
                    bounce_type = Bullet.bullets[bullet_index].check_wall_collision_type(collided_wall)

                    # Bounce said bullets accordingly
                    if (bounce_type == 0):
                        Bullet.bullets[bullet_index].angle = 180 - Bullet.bullets[bullet_index].angle

                    elif (bounce_type == 1):
                        Bullet.bullets[bullet_index].angle = -Bullet.bullets[bullet_index].angle
                else:
                    # Onto the next bullet
                    bullet_index += 1 

            
        # Make the background Black
        self.window.fill(self.background_color)

        # Try to delete a wall
        Wall.delete(self.clock_cycle)
        
        # Draw out the walls
        for i in range(len(Wall.walls)):
            Wall.walls[i].draw(self.window)

        # Draw out each player's sprite 
        for i in range(len(Player.players)):
            Player.players[i].draw(self.window)
        
        # Draw out the bullets
        for i in range(len(Bullet.bullets)):
            Bullet.bullets[i].draw(self.window)

        # Show the text onscreen
        self.window.blit(text, textRect)

    def run(self):
        # Check if the scene needs to be initialized
        first_time = (self.mode != self.last_mode)
        self.last_mode = self.mode 

        scenes = [self.titlescreen,self.gameplay]

        # Run the scene
        scenes[self.mode](first_time)
