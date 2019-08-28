import pygame

import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, player):
        self.screen = screen
        self.x = x
        self.y = y
        self.player = player
        self.hurtImage = pygame.image.load("../assets/"")
        self.image = pygame.image.load("../assets/"")
        self.rect = self.image.get_rect
        self.rect.center = (self.x, self.y)
        self.angle = 0
        self.speed = 2.5
        self.health = 50
    def update(self, projectile):

        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.player.x, self.player.y )

        angle._rads = math.radians(self.angle)
        self.x _move = math.cos(angle_rads) * self.speed
        
