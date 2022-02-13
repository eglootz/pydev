import pygame

# Initialize the library
pygame.init()

# create a window with the size of (height=800,width=600)
screen = pygame.display.set_mode((800, 600))

# game loop
running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
