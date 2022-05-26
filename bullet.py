import math
import pygame
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

        

    def draw(self,window):
        # Draw the bullet
        pygame.draw.circle(window,self.color,(self.x, self.y),self.radius)
