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
crab_speed = 1
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

last_time = pygame.time.get_ticks()

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

    delta_time = pygame.time.get_ticks() - last_time
    last_time = pygame.time.get_ticks()
    
    if crab_x < window_width / 2:
        crab_x += crab_speed
    elif crab_x > window_width / 2:
        crab_x -= crab_speed
    if crab_y< window_height / 2:
        crab_y+= crab_speed
    elif crab_y> window_height / 2:
        crab_y-= crab_speed
    if (crab_x , crab_y) == (window_width / 2, window_height / 2):
        crab_x = randrange(window_width)
        crab_y = randrange(window_height)

    game_display.blit(bg_image, (0, 0))
    game_display.blit(player, (x,y))
    generateEnemies(crab_x , crab_y)


    pygame.display.update()
    if (time.time() - last_time >0.25):
        real_fps=fps*4
        print(fps)
        fps=0
        last_time = time.time()


pygame.quit()