#! /usr/bin/env python
#coding=utf-8
import pygame

from consts import *


class Character(pygame.sprite.Sprite):

    def __init__(self, image_file, location, realsize):
        super(Character, self).__init__()
        self.image_no = 0
        self.image = self.images[self.image_no]
    	self.image = pygame.transform.scale(pygame.image.load(self.image), realsize)
        self.rect = self.image.get_rect()
        self.rect.left = location[0] - self.rect.width / 2
        self.rect.top = location[1] - self.rect.height / 2

    def flash_image(self, image_file, delaytime):
        save = self.image
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.gameboard.blit(self.image, self.rect)
        pygame.display.update()
        pygame.time.delay(delaytime)
        self.image = save

    def update(self):
        self.image = self.next_image()
    
    def next_image(self):
        if self.image_no + 1 <= len(self.images):
            return self.images[self.image_no]
        else:
            self.image_no = 0
