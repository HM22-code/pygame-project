import pygame.sprite
import utils.assets
import configs
from enums.layers import Layers

class Logo(pygame.sprite.Sprite):
    """ Logo sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.image = utils.assets.load_sprite("logo.png")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 1), int(self.image.get_height() * 1)))
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 1.5))