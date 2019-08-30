import pygame
import image_util
import toolbox

class Base(pygame.sprite.Sprite):
    def __init__ (self, screen, x, y):
        super().__init__(self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = 0
        self.normalImage = pygame.image.load(image_util.getImage("base.png")).convert_alpha()
        self.normalImage = pygame.transform.scale(self.normalImage, (200, 900))
        self.hurtImage = pygame.image.load(image_util.getImage("Base_hurt.png")).convert_alpha()
        self.hurtImage = pygame.transform.scale(self.hurtImage, (200, 900))
        self.image = self.normalImage
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.health_max = 10000
        self.health = self.health_max
        self.health_bar_width = self.image.get_width()
        self.health_bar_hight = 20
        self.health_bar_green = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_hight)
        self.health_bar_red = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_hight)
        self.alive = True
        self.hurtTimer = 0

    def update(self, enemies):
        self.rect.center = (self.x, self.y)
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.getHit(0)
                self.getHit(enemy.damage)

        if self.hurtTimer <= 0:
            imageToRotate = self.image
        else:
            imageToRotate = self.hurtImage
            self.hurtTimer -= 1

        image_to_draw, image_rect = toolbox.getRotatedImage(imageToRotate, self.rect, self.angle)
        self.screen.blit(image_to_draw, image_rect)

        self.health_bar_red.x = self.rect.x
        self.health_bar_red.bottom = self.rect.y + 600
        pygame.draw.rect(self.screen, (255, 0, 0), self.health_bar_red)
        self.health_bar_green.topleft = self.health_bar_red.topleft
        health_percentage = self.health / self.health_max
        self.health_bar_green.width = self.health_bar_width * health_percentage
        pygame.draw.rect(self.screen, (0, 255, 0), self.health_bar_green)
        print(self.health_bar_green.top)
        print(self.health_bar_green.topleft)

    def getHit(self, damage):
        self.hurtTimer = 5
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
