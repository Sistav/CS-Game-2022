import pygame
class Player:
    players = []
    def __init__(self,movement,shoot,aim,sprite,color):
        Player.players.append(self)

        self.up = movement[0]
        self.left = movement[1]
        self.down = movement[2]
        self.right = movement[3]


        self.aim_right = aim[0]
        self.aim_left = aim[1]

        self.shoot = shoot
    

        self.velocity = 5
        self.x = 10 
        self.y = 10
        
        self.sprite = sprite

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

            self.sprite.x += self.velocity * (keys[self.right] - keys[self.left])
            self.sprite.y += self.velocity * (keys[self.down] - keys[self.up])

            # self.sprite.x = self.x
            # y = self.y
                
            self.sprite.centerx = self.sprite.centerx % window.get_width()
            self.sprite.centery = self.sprite.centery % window.get_height()

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.sprite)