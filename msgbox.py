import pygame
import sys

def draw_dialog(surface, rect, rect_color, frame_color, border_width=8, shadow_weight=12):
    rect = pygame.Rect(rect)
    frame = pygame.Rect(rect.left - border_width, rect.top - border_width, rect.w + 2 * border_width, rect.h + 2 * border_width)
    shadow = frame.move(shadow_weight, shadow_weight)
    pygame.draw.rect(surface, [0, 0, 0], shadow, 0)
    pygame.draw.rect(surface, frame_color, frame, 0)
    pygame.draw.rect(surface, rect_color, rect, 0)


class Msgbox(pygame.sprite.Sprite):

    def __init__(self, msg, location=(0,0), surface=None):
        self.font = pygame.font.Font(None,30)
        self.msg = msg
        self.surface = surface if surface else pygame.display.get_surface()
        self.x, self.y = location

    def show(self):
        draw_dialog(self.surface, (129, 155, 600, 200), (0, 255, 255), (0, 0, 200))
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