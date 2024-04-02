import pygame
import time
import random


pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('My')

running = True
x = 200
y = 200
width = 50
height = 50
vel = 3
fps=0
last_time = time.time()
black=(0,0,0)
font = pygame.font.SysFont("Arial", 26)
real_fps=0
window_width = 500
window_height = 500
ENEMY_SPEED = 2
MAX_ENEMIES = 5

game_display = pygame.display.set_mode((window_width, window_height))
bg_image = pygame.image.load('grassasset(1).png')
player = pygame.image.load('judoguy(1).png')
enemy_crab = pygame.image.load("Crab1.png")

enemies = []
def generatePalyers():
    global enemies
    x = random.randint(0,1)
    enemies.append([x,0])

def moveenemies():
    global enemies
    for enemy in enemies:
        enemies[]+=ENEMY_SPEED
def showEnemies():
    print(enemies)
    global screen
    for enemy in enemies:
        screen.blit(enemy_crab, (enemy[0],enemy[1]))


while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500-height:
        y += vel
    if keys[pygame.K_RIGHT] and x < 500-width:
        x += vel
    game_display.blit(bg_image, (0, 0))
    game_display.blit(player, (x,y))
    moveenemies()
    generatePalyers()
    showEnemies()


    pygame.display.update()
    if (time.time() - last_time >0.25):
        real_fps=fps*4
        print(fps)
        fps=0
        last_time = time.time()

    fps+=1
    txtsurf = font.render("FPS:"+str(real_fps), True, black)
    screen.blit(txtsurf,(380,10))
    pygame.display.flip()

pygame.quit()