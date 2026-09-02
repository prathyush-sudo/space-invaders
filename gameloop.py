import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10 
COLLISION_DISTANCE = 27

pygame.init()
screen =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_image = pygame.image.load('images/bg.png')
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

player_image = pygame.image.load('images/rocket.png')
player_x = PLAYER_START_X
player_y = PLAYER_START_Y
player_x_change = 0
 
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_enemies = 6
for i in range(num_enemies):
    enemy_img.append(pygame.image.load('images/enemy.png'))
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
    enemy_y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)
    
bullet_img = pygame.image.load('images/bullet.png')
bullet_x = 0
bullet_y = PLAYER_START_Y
bullet_y_change = BULLET_SPEED_Y
bullet_x_change = 0 
bullet_state = "ready"  # "ready" means the bullet is ready to be fired, "fire" means the bullet is currently moving

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10
gameover_font = pygame.font.Font('freesansbold.ttf', 64)
