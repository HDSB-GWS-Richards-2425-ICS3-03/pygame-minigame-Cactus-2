#-----------------------------------------------------------------------------
# Name:        Assignment Template (assignment.py)
# Purpose:     A description of your program goes here.
#
# Author:      Mr. Brooks
# Created:     13-Sept-2020
# Updated:     13-Sept-2020
#-----------------------------------------------------------------------------
#I think this project deserves a level XXXXXX because ...
#
#Features Added:
#   ...
#   ...
#   ...
#-----------------------------------------------------------------------------
import pygame


pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()


target_surface = pygame.Surface((100,100))
target_surface.fill('Red')
target_x = 100
target_y = 100
target_surface_area = ((target_x,target_y),(target_x + 100,target_y + 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.type != pygame.NOEVENT:
        mouse_pos = event.dict["pos"]
        if (mouse_pos)in target_surface_area:
            print ("a")
        else:
            continue

   
    screen.blit(target_surface,(target_x, target_y))


    pygame.display.update()
    clock.tick(60)

