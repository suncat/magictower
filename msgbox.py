
from choicebox import Choicebox

class Msgbox(Choicebox):
    rect_color = (0, 255, 255)
    frame_color = (0, 0, 200)

    def draw_content(self):
        super(Msgbox, self).draw_content()
        msg2 = self.font.render("Press ENTER to continue...", 1, (0, 0, 0))
        self.surface.blit(msg2, (129+self.x+200, 155+self.y+50))
    
    def response_event(self, event):
        pass
