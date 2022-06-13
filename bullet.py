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
        self.one_turn_ago_x = spawn_x
        self.one_turn_ago_y = spawn_y

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

    def check_if_center_is_in_square(self):
        for i in Wall.walls:
            if (self.x > i.x) and (self.x < (i.x + i.width)) and (self.y > i.y) and (self.y < (i.y + i.length)):
                return True
        return False
                
    def check_wall_collision(self):
        for wall in Wall.walls:
            if(self.x > (wall.x - self.radius) and self.x < (wall.x + wall.width + self.radius) and self.y >  (wall.y - self.radius) and self.y < wall.y + wall.length + self.radius):
                return wall
        return None

    def check_wall_collision_type(self,wall):
        if ((self.y + self.radius) > (wall.y + wall.length)) or (self.y - self.radius) < (wall.y):
            return 1
        else:
            return 0


            


    def draw(self,window):
        # Draw the bullet
        pygame.draw.circle(window,self.color,(self.x, self.y),self.radius)
