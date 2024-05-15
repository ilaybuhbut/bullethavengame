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
vel = 1.5
last_time = time.time()
black=(0,0,0)
font = pygame.font.SysFont("Arial", 26)
real_fps=0
ENEMY_SPEED = 2
MAX_ENEMIES = 5
score = 0

game_display = pygame.display.set_mode((window_width, window_height))
screen_gameover = pygame.display.set_mode([500, 500])
bg_image = pygame.image.load('grassasset(1).png')
player = pygame.image.load('judoguy(1).png')
crab = pygame.image.load("Crab1.png")
game_over_image = pygame.image.load('youdied.png')
game_over_image = pygame.transform.scale(game_over_image, (500, 500))

crabs = []

def generateEnemies(x,y):
    game_display.blit(crab, (x,y))

def moveCrab():
    global crabs
    for crab in crabs:
        crabs[1] += crab_speed

def highscore():
    with open("highscore.txt", "w+") as scorefile:
        highscore = scorefile.read()
        
        if len(highscore) > 0:
            highscore = int(highscore)
            if highscore < score:
                scorefile.write(str(score))
        else:
            scorefile.write(str(score))

mixer.music.load("Metro Boomin - BBL Drizzy (Lyrics) Drake Diss.mp3")

mixer.music.play(-1)

woosh = pygame.mixer.Sound("Whoosh Sounds Effects HD (No Copyright).mp3")

death = pygame.mixer.Sound("deathsound.mp3")

zawardo = pygame.mixer.Sound("ZAWARDOwordess.mp3")

last_time = pygame.time.get_ticks()
delta_time = time.time() - last_time

clock = pygame.time.Clock()

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
    if keys[pygame.K_SPACE]:
        vel += 2
        time.sleep(0.2)
        zawardo.play()
        vel -= 2
    
        

 
    

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
    game_display.blit(bg_image, (0, 0))
    game_display.blit(player, (x,y))
    generateEnemies(crab_x , crab_y)

    player_hitbox = Rect(x, y, 50, 50)
    enemy_hitbox = Rect(crab_x, crab_y, 20, 20)

    if pygame.Rect.colliderect(enemy_hitbox , player_hitbox):
        pygame.display.flip()
        clock.tick(60)
        bg_image = pygame.image.load('youdied.png')

        game_display.blit(bg_image, (0, 0))

        pygame.time.wait(1000)

        pygame.quit()
    


    score+=1
    txtsurf = font.render("score:"+str(score), True, (255,0,0))
    game_display.blit(txtsurf,(380,10))
    highscore()
    pygame.display.update()