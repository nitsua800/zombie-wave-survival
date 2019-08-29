import pygame
import random
import enemy

class Wave:
    def __init__(self, screen, amount, posX, maxY, *groups):
        #self.enemies = enemies
        print(posX)
        self.amount = amount
        self.groups = groups
        self.screen = screen
        self.posX = posX
        self.maxY = maxY

    def startWave(self, player):
        for i in range(self.amount):

            y = random.randint(20, self.maxY)
            enemy.Enemy(self.screen, self.posX, y, player)
