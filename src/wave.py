import pygame
import random
from enemy import Enemy

class Wave:
    def __init__(self, screen, amount, x, maxY, *groups):
        #self.enemies = enemies
        self.amount = amount
        self.groups = groups
        self.screen = screen
        self.x = x
        self.maxY = maxY

    def startWave(self, player):
        for i in range(self.amount):
            x = 0
            y = random.randint(0, 900)
            Enemy(self.screen, x, y, player)
