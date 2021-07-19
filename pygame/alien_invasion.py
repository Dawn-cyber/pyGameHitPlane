# -*- codeing = utf-8 -*-
# @Time : 2021/7/16 20:41
# @Author : qian
# @File：alien_invasion.py
# @Software: PyCharm
import sys
import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    #screen = pygame.display.set_mode((1200,800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height,ai_settings.screen_width))

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen,ai_settings)

    bullets = Group()


    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.updata()
        bullets.update()
        gf.updata_screen(ai_settings,screen,ship,bullets)



run_game()