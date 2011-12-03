import pygame
import sys


class Msgbox(pygame.sprite.Sprite):

    def __init__(self, msg, location=(0,0), surface=None):
        self.font = pygame.font.Font(None,30)
        self.msg = msg
        self.surface = surface if surface else pygame.display.get_surface()
        self.x, self.y = location

    def show(self):
        pygame.draw.rect(self.surface, [0, 255, 255], [129, 155, 600, 200], 0)
        warn_msg = self.font.render(self.msg, 1, (0, 0, 0))
        self.surface.blit(warn_msg, (129+self.x, 155+self.y))
        msg2 = self.font.render("Press ENTER to continue...", 1, (0, 0, 0))
        self.surface.blit(msg2, (129+self.x+200, 155+self.y+50))
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False