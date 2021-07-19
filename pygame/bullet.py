# -*- codeing = utf-8 -*-
# @Time : 2021/7/16 21:47
# @Author : qian
# @File：bullet.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):

        super(Bullet,self).__init__()

        self.screen = screen

        self.rect.centerx = ship.rect.centerxx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        self.y -=self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
