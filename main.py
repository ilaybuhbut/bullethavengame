import pygame
import time



pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('My')

running = True
x = 200
y = 200
width = 20
height = 20
vel = 1.5
fps=0
last_time = time.time()
black=(0,0,0)
font = pygame.font.SysFont("Arial", 26)
real_fps=0
window_width = 500
window_height = 500
game_display = pygame.display.set_mode((window_width, window_height))
bg_image = pygame.image.load('grassasset(1).png')
player = pygame.image.load('bettersquid.png')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_display.blit(bg_image, (0, 0))
    game_display.blit(player, (x,y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500-height:
        y += vel
    if keys[pygame.K_RIGHT] and x < 500-width:
        x += vel

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