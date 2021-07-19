# -*- codeing = utf-8 -*-
# @Time : 2021/7/16 21:05
# @Author : qian
# @File：game_functions.py
# @Software: PyCharm
import sys
import pygame
import ship

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def updata_screen(ai_settings,screen,ship,bullets):

    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()

def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

