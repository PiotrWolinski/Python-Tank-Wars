import pygame
import timeit
from projectile import Projectile

class Tank:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    SPEED = 8
    RELOAD = 300

    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.last_move = 0
        self.projectiles = []
        self.load_icons()
        self.buf = 0
        
    def load_icons(self):
        self.icons = []
        self.icons.append(pygame.image.load('player\\player_up.png'))
        self.icons.append(pygame.image.load('player\\player_right.png'))
        self.icons.append(pygame.image.load('player\\player_down.png'))
        self.icons.append(pygame.image.load('player\\player_left.png'))
        
        for index, icon in enumerate(self.icons):
            self.icons[index] = pygame.transform.scale(self.icons[index], (64, 64))

    def move(self, direction):
        if direction == Tank.UP and self.y > 0:                            # up
            self.y -= Tank.SPEED
        elif direction == Tank.RIGHT and self.x < self.size_x - 64:        # right
            self.x += Tank.SPEED
        elif direction == Tank.DOWN and self.y < self.size_y - 64:         # down
            self.y += Tank.SPEED
        elif direction == Tank.LEFT and self.x > 0:                        # left
            self.x -= Tank.SPEED
        self.last_move = direction

    def move_projectiles(self):
        for proj in reversed(self.projectiles):
            proj.move()
            if not proj.if_on_map():
                self.projectiles.remove(proj)

    def print_player(self, screen):
        screen.blit(self.icons[self.last_move], (self.x, self.y))

        for proj in self.projectiles:
            proj.print_projectile(screen)

    def shoot(self):
        if not self.buf:
            self.projectiles.append(Projectile(self.x + 24, self.y + 24, self.size_x, self.size_y, self.last_move))
            self.buf = Tank.RELOAD

    def reload(self, tick):
        self.buf = self.buf - tick if self.buf > 0 else 0
