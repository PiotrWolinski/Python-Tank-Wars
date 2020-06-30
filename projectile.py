import pygame

class Projectile:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    SPEED = 24

    def __init__(self, x, y, size_x, size_y, direction):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.direction = direction
        self.on_map = True

        self.load_icons()

    def load_icons(self):
        self.icons = []
        self.icons.append(pygame.image.load('projectile\\projectile_up.png'))
        self.icons.append(pygame.image.load('projectile\\projectile_right.png'))
        self.icons.append(pygame.image.load('projectile\\projectile_down.png'))
        self.icons.append(pygame.image.load('projectile\\projectile_left.png'))
        
        for index, icon in enumerate(self.icons):
            self.icons[index] = pygame.transform.scale(self.icons[index], (16, 16))
    
    def move(self):
        if self.direction == Projectile.UP:
            self.y -= Projectile.SPEED
        elif self.direction == Projectile.RIGHT:
            self.x += Projectile.SPEED
        elif self.direction == Projectile.DOWN:
            self.y += Projectile.SPEED
        elif self.direction == Projectile.LEFT:
            self.x -= Projectile.SPEED
        
        if self.x < - 16 or self.x > self.size_x or self.y < -16 or self.y > self.size_y:
            self.on_map = False

    def print_projectile(self, screen):
        screen.blit(self.icons[self.direction], (self.x, self.y))

    def if_on_map(self):
        return self.on_map