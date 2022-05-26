import pygame
class Player:
    players = []
    def __init__(self,movement,shoot,aim,sprite,color):
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
        
        # Set sprite and sprite color
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
                
            # Create Wrapping Effect
            self.sprite.centerx = self.sprite.centerx % window.get_width()
            self.sprite.centery = self.sprite.centery % window.get_height()

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.sprite)