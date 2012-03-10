import pygame, sys


def draw_dialog(surface, rect, rect_color, frame_color, border_width=8, shadow_weight=12):
    rect = pygame.Rect(rect)
    frame = pygame.Rect(rect.left - border_width, rect.top - border_width, rect.w + 2 * border_width, rect.h + 2 * border_width)
    shadow = frame.move(shadow_weight, shadow_weight)
    pygame.draw.rect(surface, [0, 0, 0], shadow, 0)
    pygame.draw.rect(surface, frame_color, frame, 0)
    pygame.draw.rect(surface, rect_color, rect, 0)


class Choicebox(object):
    rect_color = (255, 255, 0)
    frame_color = (255, 127, 0)

    def __init__(self, msgs, location=(0,0), surface=None):
        self.font = pygame.font.Font(None,30)
        if isinstance(msgs, (list, tuple)):
            self.msgs = msgs
        elif isinstance(msgs, (str, unicode)):
            self.msgs = [msgs]
        else:
            raise TypeError('Error type of parameter msgs.')
        self.surface = surface if surface else pygame.display.get_surface()
        self.x, self.y = location

    def _draw_msgs(self):
        draw_dialog(self.surface, [129, 155, 600, 200], self.rect_color, self.frame_color)
        y = 155 + self.y
        for msg in self.msgs:
            choice_msg = self.font.render(msg, 1, (0, 0, 0))
            self.surface.blit(choice_msg, (129 + self.x, y))
            y += 30

    def show(self, player, d):
        self._draw_msgs()
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    m = d.get(event.key)
                    if m is not None:
                        getattr(player, m)()
                    waiting = False
