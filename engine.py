import pygame
import sys
import os.path
import random

pygame.init()
pygame.mixer.init()


class Scene(object):
    
    def __init__(self, screen):
        self.screen = screen


class Game(object):
    musics = []
    
    def __init__(self, screen_width, screen_height, fps=30, keyrepeat=True):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.root = pygame.sprite.Group()
        self.fps = fps
        if keyrepeat:
            pygame.key.set_repeat(100, 50)
        self.scenes = []
        
    def run(self):
        self.extra_init()
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.response_event(event)
                    for obj in self.root:
                        if hasattr(obj, 'response_event'):
                            obj.response_event(event)
            self.bgmusic()
            self.update()
            self.animate()
            self.draw()
            pygame.display.flip()
        pygame.quit()
        
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
        self.root.update()
    
    def animate(self):
        for obj in self.root:
            obj.animate()
            
    def draw(self):
        self.root.update()

    def add_scene(self, scene):
        self.scenes.append(scene)
        
        
if __name__ == '__main__':
    game = Game(640,480)
    game.run()