import pygame
import math
import image_util

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, base):
        self.screen = screen
        self.x = x
        self.y = y
        self.base = base
        self.hurtImage = pygame.image.load(image_util.getImage("Walker_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Walker.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = 0
        self.speed = 5
        self.health = 50

    def update(self, projectiles):
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.image, self.rect)
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.player.x, self.player.y )
        angle._rads = math.radians(self.angle)
        self.x_move = math.cos(angle_rads) * self.speed
        self.y_move = math.sin(angle_rads) * self.speed
        self.x += self.x_move
        self.y += self.y_move
        self.rect.center = (self.x, self.y)

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
        self.image = self.imageHurt
        if self.health <= 0:
            self.health = 9999
            self.kill()

class Brute(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Brute_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Brute.png"))
        self.speed = 2
        self.health = 100

class Crawler(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Crawler_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Crawler.png"))
        self.speed = 1.5
        self.health = 75

class Helicopter(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Helicoptere_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Helicopter.png"))
        self.speed = 3
        self.health = 60

class Spider(Enemy):
    def __init__(self, screen, x, y, base):
        super().__init__(screen, x, y, base)
        self.hurtImage = pygame.image.load(image_util.getImage("Spider_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Spider.png"))
        self.speed = 10
        self.health = 45
