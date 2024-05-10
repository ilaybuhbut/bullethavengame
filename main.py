import pygame
from pygame import mixer
import time
import random
from random import randrange
import subprocess
from pygame import Rect
pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('dodging game?')

running = True
x = 250
y = 250
window_width = 500
window_height = 500
width = 50
height = 50
crab_x = randrange(window_width)
crab_y = randrange(window_height)
crab_speed = 0.5
vel = 1
last_time = time.time()
black=(0,0,0)
font = pygame.font.SysFont("Arial", 26)
real_fps=0
ENEMY_SPEED = 2
MAX_ENEMIES = 5
score = 0

game_display = pygame.display.set_mode((window_width, window_height))
bg_image = pygame.image.load('bullethavengame\\grassasset(1).png')
player = pygame.image.load('bullethavengame\\judoguy(1).png')
crab = pygame.image.load("bullethavengame\\Crab1.png")


crabs = []

def generateEnemies(x,y):
    game_display.blit(crab, (x,y))

def moveCrab():
    global crabs
    for crab in crabs:
        crabs[1] += crab_speed

mixer.music.load("Metro Boomin - BBL Drizzy (Lyrics) Drake Diss.mp3")

mixer.music.play(-1)

woosh = pygame.mixer.Sound("Whoosh Sounds Effects HD (No Copyright).mp3")

last_time = pygame.time.get_ticks()
delta_time = time.time() - last_time
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
    if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
        vel += 2
        woosh.play()
        vel -= 2


    
        
          
    delta_time = pygame.time.get_ticks() - last_time
    last_time = pygame.time.get_ticks()

#**************************************************************************
#movemnt
    if crab_x < window_width / 2:
        crab_x += crab_speed
    elif crab_x > window_width / 2:
        crab_x -= crab_speed
    if crab_y< window_height / 2:
        crab_y+= crab_speed
    elif crab_y> window_height / 2:
        crab_y -= crab_speed
    #
    if (crab_x , crab_y) == (window_width / 2, window_height / 2):
        crab_x = randrange(window_width)
        crab_y = randrange(window_height)
#**************************************************************************

    player_hitbox = Rect(x, y, 50, 50)
    enemy_hitbox = Rect(crab_x, crab_y, 20, 20)

    if pygame.Rect.colliderect(enemy_hitbox , player_hitbox):
        subprocess.run(["msg" , "*" , "you lost lol"])

        pygame.quit()
    
    game_display.blit(bg_image, (0, 0))
    game_display.blit(player, (x,y))
    generateEnemies(crab_x , crab_y)


    score+=1
    txtsurf = font.render("score:"+str(score), True, (255,0,0))
    game_display.blit(txtsurf,(380,10))
    pygame.display.update()


pygame.quit()