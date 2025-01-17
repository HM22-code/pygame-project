import pygame.sprite
import utils.assets
import configs
from enums.layers import Layers

class ParallaxLayer(pygame.sprite.Sprite):
    """ ParallaxLayer sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, level: int, index: int, *groups):
        super().__init__(*groups)
        self._layer = Layers.BACKGROUND
        self.image = utils.assets.get_sprite("parallax-"+str(level)+".png")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))
        self.level = level
        self.speed = 5
    
    def update(self, dt):
        self.rect.x -= (self.speed//self.level)
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH