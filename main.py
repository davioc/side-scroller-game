import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen with color and wipe away previous frame
    screen.fill("white")

    # flip() displays content on screen
    pygame.display.flip()

    clock.tick(60) # limit to 60 FPS

pygame.quit()