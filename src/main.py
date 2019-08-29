import pygame
import image_util
from player import Player
from projectile import Bullet
from enemy import Enemy
from wave import Wave
# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
background_image = pygame.image.load(image_util.getImage("landscape.png")).convert()

playerGroup = pygame.sprite.Group()
projectilesGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()

Player.containers = playerGroup
Bullet.containers = projectilesGroup
Enemy.containers = enemiesGroup

mr_player = Player(screen, game_width/2, game_height/2)

wave = Wave(screen, 5, enemiesGroup, game_width, game_height)

# Enemy(screen, 100, 100, mr_player)
# Enemy(screen, 100, 500, mr_player)


wave.startWave(mr_player)
# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        mr_player.move(1, 0)
    if keys[pygame.K_a]:
        mr_player.move(-1, 0)
    if keys[pygame.K_w]:
        mr_player.move(0, -1)
    if keys[pygame.K_s]:
        mr_player.move(0, 1)
    if pygame.mouse.get_pressed()[0]:
        mr_player.shoot()

    screen.blit(background_image, (0, 0))

    mr_player.update()

    for projectile in projectilesGroup:
        projectile.update()
    for enemy in enemiesGroup:
        enemy.update(projectilesGroup)

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption("Zombie Shooter fps: " + str(clock.get_fps()))
    
