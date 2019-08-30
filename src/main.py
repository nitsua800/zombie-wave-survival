import pygame
import image_util
from player import Player
from projectile import Bullet
import enemy
from wave_controller import WaveController
from score_manager import ScoreManager
from base import Base
# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
background_image = pygame.image.load(image_util.getImage("landscape.png")).convert()
waveComing = False

playerGroup = pygame.sprite.Group()
projectilesGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
baseGroup = pygame.sprite.Group()

Player.containers = playerGroup
Bullet.containers = projectilesGroup
enemy.Enemy.containers = enemiesGroup
Base.containers = baseGroup
mr_player = Player(screen, 180, game_height/2)
base = Base(screen, 100, game_height/2)
wave_controller = WaveController(screen, game_width, game_height, enemiesGroup)

pygame.mixer.music.load(image_util.getImage('Main_Theme.wav'))
pygame.mixer.music.play(-1)

font = pygame.font.SysFont('Bodoni 72 Book', 60)
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
    if keys[pygame.K_p]:
        if not waveComing:
            waveComing = True
            wave_controller.new_wave(base)

    screen.blit(background_image, (0, 0))
    base.update(enemiesGroup)
    mr_player.update()

    for projectile in projectilesGroup:
        projectile.update()
    for enemy in enemiesGroup:
        enemy.update(projectilesGroup)

    if not enemiesGroup.sprites():
        waveComing = False

    score_text = font.render("Score: " + str(ScoreManager.score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    wave_text = font.render("Wave: " + str(wave_controller.wave_number), True, (255, 255, 255))
    screen.blit(wave_text, (800, 10))

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption("Zombie Shooter fps: " + str(clock.get_fps()))
