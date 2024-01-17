import pygame.sprite
import assets
import configs
from layers import Layers

class Background(pygame.sprite.Sprite):
    
    def __init__(self, index, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))
        
    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH