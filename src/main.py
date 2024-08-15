import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Side Scroller')

# helps control the frame rate
clock = pygame.time.Clock()
running = True
dt = 0

background_surface = pygame.image.load('src/graphics/cloud.png')
ground_surface = pygame.image.load('src/graphics/ground.png')

# player starting position
player_pos = pygame.Vector2(40, 660)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # blit = "block image transfer"
    screen.blit(background_surface,(0,0))
    screen.blit(ground_surface,(0,700))
    
    # fill screen with color and wipe away previous frame
    # screen.fill("white")

    # flip() displays content on screen
    pygame.draw.circle(screen, "grey", player_pos, 40)
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.update()
    # clock.tick(60) sets 60 FPS limit
    dt = clock.tick(60) / 1000
    # pygame.display.flip()

pygame.quit()