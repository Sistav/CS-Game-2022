import math
import pygame
class Bullet:
    bullets = []
    def __init__(self,spawn_x,spawn_y,angle, color,spawn_tick):
        Bullet.bullets.append(self)
        self.x = spawn_x
        self.y = spawn_y
        
        self.angle = angle
        self.color = color
        
        self.speed = 5
        self.radius = 10
        
        self.spawn_tick = spawn_tick
        
        self.lifetime =  20 * 60

    def move(self,window,current_cycle):
        rad_angle = self.angle * math.pi / 180
        self.x += self.speed * math.cos(rad_angle)
        self.y += self.speed * -math.sin(rad_angle)

        self.x = self.x % window.get_width()
        self.y = self.y % window.get_height()

        

    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x, self.y),self.radius)
