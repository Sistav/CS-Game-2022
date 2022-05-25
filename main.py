import sys, pygame
pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

rect1 = pygame.Rect(0, 0, 20, 20)

rect2 = pygame.Rect(0, 0, 20, 20)

player1 = Player(pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d)
player2 = Player(pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    keys = pygame.key.get_pressed()
    

black = 0, 0, 0

screen = pygame.display.set_mode(size)

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()


    pygame.display.flip()