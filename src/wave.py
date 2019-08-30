import pygame
import random
import enemy

class Wave:
    def __init__(self, enemies, screen, amount, posX, maxY, *groups):
        self.enemies = enemies
        self.amount = amount
        self.groups = groups
        self.screen = screen
        self.posX = posX
        self.maxY = maxY

    def startWave(self, target):
        for i in range(self.amount):
            x = random.randint(self.posX, self.posX + 100)
            y = random.randint(20, self.maxY)

            index = random.randint(0, len(self.enemies) - 1)
            type  = self.enemies[index]
            if type == "walker":
                enemy.Enemy(self.screen, x, y, target)
            elif type == "crawler":
                enemy.Crawler(self.screen, x, y, target)
            elif type == "brute":
                enemy.Brute(self.screen, x, y, target)
            elif type == "spider":
                enemy.Spider(self.screen, x, y, target)
            elif type == "runner":
                enemy.Runner(self.screen, x, y, target)
            elif type == "motorcycle":
                enemy.Motorcycle(self.screen, x, y, target)
            elif type == "helicopter":
                enemy.Helicopter(self.screen, x, y, target)
