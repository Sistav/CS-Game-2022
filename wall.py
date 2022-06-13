import pygame
import random
class Wall:
    divisor = 8

    # Time in frames for how long to delete a wall
    lifetime = 5 * 60

    walls = []
    def __init__(self,x,y,width,length):
        Wall.walls.append(self)

        self.x = x
        self.y = y

        
        self.width = width
        self.length = length

        self.color = "white"


    def generate(length,width):
        no_wall_area = []
        upper = 2

        wall_width = width/Wall.divisor
        wall_length = length/Wall.divisor

        for i in range(Wall.divisor):
            
            for j in range(Wall.divisor):
                    x = i*(wall_width)
                    y = j*(wall_length)
                    if random.randint(0, upper-1) == 0:
                        Wall(x,y,wall_width,wall_length)
                    else:
                        no_wall_area.append(((x+(x+wall_width))/2,((y+(y+wall_length))/2)))
                        
        return no_wall_area
                
    def delete(clock_cycle):
        if len(Wall.walls) > 0:
            if ((clock_cycle % Wall.lifetime) == 0):
                del Wall.walls[random.randint(0,len(Wall.walls)-1)]

    def draw(self,window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.width, self.length))
                