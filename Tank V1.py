import pygame
import random
import math

GRAD = math.pi/180
pygame.init()
x        = 800
y        = 800
white    = (255,255,255)
black    = (0,0,0)
red      = (255,0,0)
green    = (0,145,0)
brown    = (165,45,45)
blue     = (0,0,255)
purple   = (198,86,198)
tick     = 15

player_x = 10
player_y = 10

clock = pygame.time.Clock()
window= pygame.display.set_mode((x,y))
pygame.display.set_caption("Tanks")
font = pygame.font.SysFont(None,25)
tank = pygame.image.load("assets\\tank2.png")



def text_to_screen(msg,colour):
    screen_text = font.render(msg, True, colour)
    window.blit(screen_text,[x/2,y/2])

def rotate(image,angle):
    orig_rect  = image.get_rect()
    rot_image  = pygame.transform.rotate(image,angle)
    rot_rect   = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def gameLoop():
    game_quit=False
    speed = 0
    rot   = 0
    rot_change = 0
    speed_change=0
    tankposx = x/2
    tankposy = y/2
    while 1:
        window.fill(green)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and speed <=  5:
                    speed_change += 1

                if event.key == pygame.K_DOWN and speed >= -5:
                    speed_change -= 1
                if event.key == pygame.K_RIGHT:
                    rot_change -= 10
                if event.key == pygame.K_LEFT:
                    rot_change += 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    speed_change=0
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    rot_change = 0
        speed += speed_change
        rot +=rot_change
        if game_quit == True:
            pygame.quit()
            quit()
        print(rot)
        rotank = rotate(tank,rot)
        window.blit(rotank,(tankposx,tankposy))
        tankposx -= speed * math.sin(rot*GRAD)
        tankposy -= speed * math.cos(rot*GRAD)



        pygame.display.update()
        clock.tick(tick)


gameLoop()