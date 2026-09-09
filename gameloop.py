import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64
ENEMY_WIDTH = 80
ENEMY_HEIGHT = 80
BULLET_WIDTH = 18
BULLET_HEIGHT = 32
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 1
ENEMY_SPEED_Y = 0.1
BULLET_SPEED_Y = 10 
COLLISION_DISTANCE = 50

pygame.init()
screen =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_image = pygame.transform.scale(pygame.image.load('images/bg.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
icon = pygame.transform.scale(pygame.image.load('images/ufo.png').convert_alpha(), (40, 40))
pygame.display.set_icon(icon)

player_image = pygame.transform.scale(pygame.image.load('images/rocket.png').convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT))
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
    enemy_img.append(pygame.transform.scale(pygame.image.load('images/enemy.png').convert_alpha(), (ENEMY_WIDTH, ENEMY_HEIGHT)))
    enemy_x.append(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH))
    enemy_y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)
    
bullet_img = pygame.transform.scale(pygame.image.load('images/bullets.png').convert_alpha(), (BULLET_WIDTH, BULLET_HEIGHT))
bullet_x = 0
bullet_y = PLAYER_START_Y
bullet_y_change = BULLET_SPEED_Y
bullet_x_change = 0 
bullet_state = "ready"  # "ready" means the bullet is ready to be fired, "fire" means the bullet is currently moving

score_value = 0
font = pygame.font.Font(r"C:\Windows\Fonts\arial.ttf", 32)
text_x = 10
text_y = 10
gameover_font = pygame.font.Font(r"C:\Windows\Fonts\arial.ttf", 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
    
def game_over_text():
    over_text = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    
def player(x,y):
    screen.blit(player_image, (x, y))
    
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(((enemy_x - bullet_x) ** 2) + ((enemy_y - bullet_y) ** 2))
    return distance < COLLISION_DISTANCE

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
                
    player_x += player_x_change
    player_x = max(0, min(player_x, SCREEN_WIDTH - PLAYER_WIDTH))  # Keep player within screen bounds
    
    
    # Enemy movement
    for i in range(num_enemies):
        # Game over condition
        if enemy_y[i] > 340:
            for j in range(num_enemies):
                enemy_y[j] = 2000  # Move enemies off-screen
            game_over_text()
            break
        
        enemy_x[i] += enemy_x_change[i]
        
        # Enemy boundary checking
        if enemy_x[i] <= 0 or enemy_x[i] >= SCREEN_WIDTH - ENEMY_WIDTH:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]
            
        
        # Collision detection
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemy_y[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        
        enemy(enemy_x[i], enemy_y[i], i)
    
    # Bullet movement
    if bullet_y <= 0:
        bullet_y = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
    
#peace out