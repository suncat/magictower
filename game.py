import pygame
import sys
import os.path
import random

pygame.init()
pygame.mixer.init()


class Game:
    musics = []
    
    def __init__(self, screen_width, screen_height, fps=30, keyrepeat=True):
        self.width = screen_width
        self.height = screen_height
        self.fps = fps
        if keyrepeat:
            pygame.key.set_repeat(100, 50)
        
    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.extra_init()
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    self.response_event(event)
            self.bgmusic()
            self.update()
            self.draw()
            pygame.display.flip()
            
    def extra_init(self):
        pass
    
    def response_event(self, event):
        pass
    
    def bgmusic(self):
        if not self.musics:
            return
        if not pygame.mixer.music.get_busy():
             music = random.choice(self.musics)
             pygame.mixer.music.load(os.path.join("sound", music))
             pygame.mixer.music.play()
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
if __name__ == '__main__':
    game = Game(640,480)
    game.run()