import pygame
import math
import toolbox
import image_util

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, target):
        super().__init__(self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.target = target
        self.normalImage = pygame.image.load(image_util.getImage("Walker.png")).convert_alpha()
        self.hurtImage = pygame.image.load(image_util.getImage("Walker_hurt.png")).convert_alpha()
        self.image = self.normalImage
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = 0
        self.speed = 5
        self.health = 10

    def update(self, projectiles):
        self.x_move = 0.1 * self.speed
        self.y_move = 0
        self.x += self.x_move
        self.rect.center = (self.x, self.y)
        self.image = self.normalImage

        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.getHit(projectile.damage)
                projectile.explode()

        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.screen.blit(image_to_draw, image_rect)

    def getHit(self, damage):
        self.x -= self.x_move * 5
        self.y -= self.y_move * 5
        self.health -= damage
        self.image = self.hurtImage
        if self.health <= 0:
            self.health = 9999
            self.kill()

class Brute(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Brute_hurt.png")).convert_alpha()
        self.image = pygame.image.load(image_util.getImage("Brute.png")).convert_alpha()
        self.speed = 2
        self.health = 100

class Crawler(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Crawler_hurt.png")).convert_alpha()
        self.image = pygame.image.load(image_util.getImage("Crawler.png")).convert_alpha()
        self.speed = 1.5
        self.health = 75

class Helicopter(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Helicoptere_hurt.png")).convert_alpha()
        self.image = pygame.image.load(image_util.getImage("Helicopter.png")).convert_alpha()
        self.speed = 3
        self.health = 80

class Spider(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Spider_hurt.png")).convert_alpha()
        self.image = pygame.image.load(image_util.getImage("Spider.png")).convert_alpha()
        self.speed = 10
        self.health = 45
class Runner(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Runner_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Runner.png"))
        self.speed = 100
        self.health = 15
class Motorcycle(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Motorcycle_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Motorcycle.png"))
        self.speed = 15
        self.health = 45
