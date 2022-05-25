class Player:
    players = []
    def __init__(self,up,left,down,right):
        Player.players.append(self)

        self.up = up
        self.left = left
        self.down = down
        self.right = right

        self.velocity = 5
        self.x = 10 
        self.y = 10
    
    def check_movement(self,keys):
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