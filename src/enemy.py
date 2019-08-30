import pygame
import math
import toolbox
from score_manager import ScoreManager
import image_util

class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, target):
        super().__init__(self.containers)
        self.screen = screen
        self.target = target
        self.x = x
        self.y = y
        self.normalImage = pygame.image.load(image_util.getImage("Walker.png")).convert_alpha()
        self.hurtImage = pygame.image.load(image_util.getImage("Walker_hurt.png")).convert_alpha()
        self.image = self.normalImage
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = 180
        self.speed = 5
        self.health = 50
        self.damage = 10
        self.hurtTimer = 0

    def update(self, projectiles):
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.target.x, self.y)
        angle_rads = math.radians(self.angle)
        self.x_move = (math.cos(angle_rads) / 5) * self.speed
        self.y_move = 0
        self.x += self.x_move
        self.y += self.y_move
        self.rect.center = (self.x, self.y)
        self.image = self.normalImage

        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.getHit(projectile.damage)
                projectile.explode()

        if self.hurtTimer <= 0:
            imageToRotate = self.image
        else:
            imageToRotate = self.hurtImage
            self.hurtTimer -= 1

        image_to_draw, image_rect = toolbox.getRotatedImage(imageToRotate, self.rect, self.angle)
        self.screen.blit(image_to_draw, image_rect)

    def getHit(self, damage):
        if damage:
            toolbox.playSound('hit.wav')
            self.hurtTimer = 5
        self.x -= self.x_move * 10
        self.y -= self.y_move * 10
        self.health -= damage
        if self.health <= 0:
            self.health = 9999
            self.kill()
            toolbox.playSound('point.wav')
            ScoreManager.score += 1


class Brute(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.normalImage = pygame.image.load(image_util.getImage("Brute.png")).convert_alpha()
        self.hurtImage = pygame.image.load(image_util.getImage("Brute_hurt.png")).convert_alpha()
        self.image = self.normalImage
        self.speed = 2
        self.health = 100

class Crawler(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Crawler_hurt.png")).convert_alpha()
        self.normalImage = self.normalImage
        self.normalImage = pygame.image.load(image_util.getImage("Crawler.png")).convert_alpha()
        self.speed = 1.5
        self.health = 75
        self.angle = 90

class Helicopter(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("helicopter_hurt.png")).convert_alpha()
        self.normalImage = pygame.image.load(image_util.getImage("helicopter.png")).convert_alpha()
        self.normalImage = pygame.transform.scale(self.normalImage, (40, 40))
        self.normalImage = self.normalImage
        self.speed = 3
        self.health = 80

class Spider(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Spider_hurt.png")).convert_alpha()
        self.image = pygame.image.load(image_util.getImage("Spider.png")).convert_alpha()
        self.speed = 10
        self.health = 45
class Runner(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Runner_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Runner.png"))
        self.speed = 100
        self.health = 15
class Motorcycle(Enemy):
    def __init__(self, screen, x, y, target):
        super().__init__(screen, x, y, target)
        self.hurtImage = pygame.image.load(image_util.getImage("Motorcycle_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Motorcycle.png"))
        self.speed = 15
        self.health = 45
