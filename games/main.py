import pygame

# Initialize the library
pygame.init()

# create a window with the size of (width=800,height=600)
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("Space Invader")

# Player
playerImg = pygame.image.load("bird.png")
playerX = 370
playerY = 480


def Player():
    screen.blit(playerImg, (playerX, playerY))


# game loop
running = True
while(running):

    # RGB screen fill
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Player()
    pygame.display.update()
