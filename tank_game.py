import pygame
import sys 
from tank_class import Tank
from projectile import Projectile

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
        if pressed[pygame.K_SPACE]:
            tank.shoot()
    elif pressed[pygame.K_RIGHT]:
        tank.move(Tank.RIGHT)
        if pressed[pygame.K_SPACE]:
            tank.shoot()
    elif pressed[pygame.K_DOWN]:
        tank.move(Tank.DOWN)
        if pressed[pygame.K_SPACE]:
            tank.shoot()
    elif pressed[pygame.K_LEFT]:
        tank.move(Tank.LEFT)
        if pressed[pygame.K_SPACE]:
            tank.shoot()
    elif pressed[pygame.K_SPACE]:
        tank.shoot()
    elif pressed[pygame.K_ESCAPE]:
        running = False
        sys.exit(0)
    
    screen.fill((255, 255, 255))
    
    tank.print_player(screen)
    tank.move_projectiles()
    tank.reload(FPS)

    pygame.display.update()
    clock.tick(FPS)