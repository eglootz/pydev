import pygame

# Initialize the library
pygame.init()

# create a window with the size of (height=800,width=600)
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("Space Invader")


# game loop
running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB screen fill
    screen.fill((0, 0, 0))
    pygame.display.update()
