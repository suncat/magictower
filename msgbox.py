import pygame
import sys

from choicebox import Choicebox, draw_dialog

class Msgbox(Choicebox):
    rect_color = (0, 255, 255)
    frame_color = (0, 0, 200)

    def show(self):
        self._draw_msgs()
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