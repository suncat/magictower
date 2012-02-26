#! /usr/bin/env python
#coding=utf-8
import pygame

from consts import *


class Character(pygame.sprite.Sprite):
    images = []

    def __init__(self, location, realsize):
        super(Character, self).__init__()
        self.images = [pygame.transform.scale(pygame.image.load(imagefile), realsize) for imagefile in self.images]
        self.image_no = 0
        self.image = self.images[self.image_no]
        self.update_counter = 10
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
        self.update_counter -= 1
        if self.update_counter ==0:
            self.image = self.next_image()
            self.update_counter = 10
    
    def next_image(self):
        if self.image_no + 1 < len(self.images):
            self.image_no += 1
        else:
            self.image_no = 0
        return self.images[self.image_no]
