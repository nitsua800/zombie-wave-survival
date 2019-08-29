import pygame
import math
import image_util

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, player):
        self.screen = screen
        self.x = x
        self.y = y
        self.player = player
        self.hurtImage = pygame.image.load(image_util.getImage("Walker_hurt.png"))
        self.image = pygame.image.load(image_util.getImage("Walker.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = 0
        self.speed = 2.5
        self.health = 50
    def update(self, projectile):
class Brute(Enemy):

class Crawler(Enemy):

class helicopter(Enemy):

class Spider(Enemy):

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
        self.hurtImage = pygame.image.load(image_util.getImage("Walker_hurt.png"))
        if self.health <= 0:
            self.health = 9999
            self.kill()
