import math
import pygame
from wall import *
class Bullet:
    bullets = []
    def __init__(self,spawn_x,spawn_y,angle, color,spawn_tick):
        Bullet.bullets.append(self)
        
        # angle the bullet was shot at and it's spawn coords
        self.x = spawn_x
        self.y = spawn_y
        self.angle = angle

        # Set color of the bullet
        self.color = color
        
        # Speed in which the bullet moves
        self.speed = 5
        
        # Set the size of the bullet
        self.radius = 10
        
        # This is the tick that the bullet spawned at
        self.spawn_tick = spawn_tick
        
        # Set time till death in  frames (left is seconds)
        self.lifetime =  20 * 60

    def move(self,window):
        # Calculate the slope and move bullet accordingly
        rad_angle = self.angle * math.pi / 180
        self.x += self.speed * math.cos(rad_angle)
        self.y += self.speed * -math.sin(rad_angle)

        # Wrap bullet around
        self.x = self.x % window.get_width()
        self.y = self.y % window.get_height()


    def check_wall_collision(self):
        wall_index = 0
        while wall_index < len(Wall.walls) - 1:

            dist_x = abs(self.x - Wall.walls[wall_index].x - Wall.walls[wall_index].width/2);
            dist_y = abs(self.y - Wall.walls[wall_index].y - Wall.walls[wall_index].length/2);

            if (dist_x > (Wall.walls[wall_index].width/2 + self.radius)) or (dist_y > (Wall.walls[wall_index].length / 2 + self.radius)):
                wall_index += 1 
            
            if (dist_x <= (Wall.walls[wall_index].width/2)) or (dist_y <= (Wall.walls[wall_index].length/2)): 
                # collided
               return True
            
            dx = dist_x  -Wall.walls[wall_index].width / 2
            dy = dist_y - Wall.walls[wall_index].length / 2

            if ((dx ** 2) + (dy ** 2) <= (self.radius ** 2)):
                # collided
                return True

            else:
                wall_index += 1
        return False


    def draw(self,window):
        # Draw the bullet
        pygame.draw.circle(window,self.color,(self.x, self.y),self.radius)
