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
        self.health = 1000
        self.normalImage = pygame.image.load(image_util.getImage("base.png")).convert_alpha()
        self.normalImage = pygame.transform.scale(self.normalImage, (200, 900))
        self.hurtImage = pygame.image.load(image_util.getImage("Walker_hurt.png")).convert_alpha()
        self.image = self.normalImage
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        self.rect.center = (self.x, self.y)

        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.screen.blit(image_to_draw, image_rect)
