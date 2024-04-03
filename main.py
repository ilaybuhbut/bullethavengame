import pygame
import time
import random
from random import randrange

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('dodging game?')

running = True
x = 200
y = 200
window_width = 500
window_height = 500
width = 50
height = 50
crab_x = randrange(window_width)
crab_y = randrange(window_height)
crab_speed = 2
vel = 3
fps=0
last_time = time.time()
black=(0,0,0)
font = pygame.font.SysFont("Arial", 26)
real_fps=0
ENEMY_SPEED = 2
MAX_ENEMIES = 5

game_display = pygame.display.set_mode((window_width, window_height))
bg_image = pygame.image.load('grassasset(1).png')
player = pygame.image.load('judoguy(1).png')
crab = pygame.image.load("Crab1.png")

enemies = []
def generateEnemies(x,y):
    game_display.blit(crab, (x,y))

def moveCrab():
    global crabs
    for crab in crab:
        crabs[1]+=crab_speed

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

    crab_x += crab_speed
    crab_y += crab_speed

    if crab_x >= width:
        crab_x = randrange(window_width)
        crab_y = randrange(window_height)
    game_display.blit(bg_image, (0, 0))
    game_display.blit(player, (x,y))
    generateEnemies(crab_x , crab_y)
    crab


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