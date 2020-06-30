import pygame
import sys 
from tank_class import Tank

pygame.init()

FPS = 20
clock = pygame.time.Clock()

screen = pygame.display.set_mode((16 * 64, 12 * 64))

pygame.display.set_caption('Tank game!')
pygame.display.set_icon(pygame.image.load('tank.png'))

tank = Tank(40, 40, 16 * 64, 12 * 64)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit(0)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        tank.move(Tank.UP)
    elif pressed[pygame.K_RIGHT]:
        tank.move(Tank.RIGHT)
    elif pressed[pygame.K_DOWN]:
        tank.move(Tank.DOWN)
    elif pressed[pygame.K_LEFT]:
        tank.move(Tank.LEFT)
    elif pressed[pygame.K_ESCAPE]:
        running = False
        sys.exit(0)
    
    screen.fill((255, 255, 255))
    
    tank.print_player(screen)

    pygame.display.update()
    clock.tick(FPS)