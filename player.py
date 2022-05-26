import pygame
import math
class Player:
    players = []
    def __init__(self,movement,shoot,aim,color):
        Player.players.append(self)

        # Set Movement Controls
        self.up = movement[0]
        self.left = movement[1]
        self.down = movement[2]
        self.right = movement[3]

        # Set aim and shoot controls
        self.aim_right = aim[0]
        self.aim_left = aim[1]
        self.shoot = shoot
    
        # Set Players velocity
        self.velocity = 5

        # Set starting position
        self.x = 10 
        self.y = 10

        self.angle = 0 
        self.aim_speed = 1

        self.radius = 20        
        self.cannon_length = 50
        self.cannon_width = 10

        # Set sprite and sprite color
        # self.sprite = pygame.circle(, 40, 40)
        self.color = color
    
    def check_movement(self,keys,window):
            # if keys[self.left]:   
            #     self.x -= self.velocity
            # if keys[self.right]:
            #     self.x += self.velocity
            # if keys[self.up]:
            #     self.y -= self.velocity
            # if keys[self.down]:
            #     self.y += self.velocity

            self.x += self.velocity * (keys[self.right] - keys[self.left])
            self.y += self.velocity * (keys[self.down] - keys[self.up])

            self.angle += self.aim_speed * (keys[self.aim_left] - keys[self.aim_right]) 

            if self.angle < 0:
                self.angle += 360 
            elif self.angle > 360:
                self.angle %= 360
            print(self.angle)
            # self.sprite.x = self.x
            # y = self.y
            # Create Wrapping Effect
            self.x = self.x % window.get_width()
            self.y = self.y % window.get_height()

    def draw(self,window):
        # pygame.draw.rect(window,self.color,)
        
        rad_angle = self.angle * math.pi / 180
        self.cannon_end_x =  self.x + (self.cannon_length * math.cos(rad_angle))
        self.cannon_end_y =  self.y + (self.cannon_length * math.sin(rad_angle))
        pygame.draw.circle(window,self.color,(self.x, self.y),self.radius)

        pygame.draw.circle(window,self.color,(self.cannon_end_x, self.cannon_end_y),self.cannon_width)
        pygame.draw.line(window,self.color,(self.x, self.y), (self.cannon_end_x, self.cannon_end_y),self.cannon_width)
        