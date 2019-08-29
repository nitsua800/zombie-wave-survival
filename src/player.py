import pygame
import toolbox
import projectile
import image_util

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_util.getImage("Main_Character.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 5
        self.angle = 0
        self.shoot_cooldown = 0
        self.shoot_cooldown_max = 30


    def update(self):
        self.rect.center = (self.x, self.y)

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)

        image_to_draw, image_rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.screen.blit(image_to_draw, image_rect)

    def move (self, x_movement, y_movement):
        self.x += self.speed * x_movement
        self.y += self.speed * y_movement

    def shoot(self):
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = self.shoot_cooldown_max
            projectile.Bullet(self.screen, self.x, self.y, self.angle)
