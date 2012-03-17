import pygame

from consts import get_game
from dialog import Dialog


class Choicebox(Dialog):
    rect = (129, 155, 600, 200)
    rect_color = (255, 255, 0)
    frame_color = (255, 127, 0)

    def __init__(self,msgs, location=(0,0),  keydict={}, surface=None):
        super(Choicebox, self).__init__(self.rect, self.rect_color, frame_color=self.frame_color)
        self.keydict = keydict
        self.font = pygame.font.Font(None,30)
        if isinstance(msgs, (list, tuple)):
            self.msgs = msgs
        elif isinstance(msgs, (str, unicode)):
            self.msgs = [msgs]
        else:
            raise TypeError('Error type of parameter msgs.')
        self.x, self.y = location

    def draw_content(self):
        y = 155 + self.y
        for msg in self.msgs:
            choice_msg = self.font.render(msg, 1, (0, 0, 0))
            self.surface.blit(choice_msg, (129 + self.x, y))
            y += 30

    def response_event(self, event):
        super(Choicebox, self).response_event(event)
        if event.type == pygame.KEYDOWN:
            m = self.keydict.get(event.key)
            if m is not None:
                getattr(get_game().player, m)()
            self.closed = True