from objects.loading_bar import LoadingBar
from objects.logo import Logo
from objects.text import Text
from interfaces.state import State
from states.start import Start
import utils.assets
import pygame
import configs
import threading
import sys

class Boot(State):
    """ Boot state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.loading_bar = LoadingBar((configs.SCREEN_WIDTH - configs.LOADING_BAR_WIDTH) // 2, (configs.SCREEN_HEIGHT - configs.LOADING_BAR_HEIGHT)// 4, configs.LOADING_BAR_WIDTH, configs.LOADING_BAR_HEIGHT, configs.LOADING_BAR_MAX)
        self.sprites.add(self.loading_bar)
        self.font = "retro.ttf"
        self.sprites.add(Text(configs.SCREEN_WIDTH // 2.5, configs.SCREEN_HEIGHT // 2.5, "made with", self.font, 10, pygame.color.Color("black")))
        self.sprites.add(Logo())
        self.ready = False
        self.thread = None
    
    def load_assets(self):
        """ Load game assets and update loading bar
        """
        self.loading_bar.set_value(self.loading_bar.value + configs.LOADING_BAR_STEP)
        utils.assets.load_sprites()
        self.loading_bar.set_value(self.loading_bar.value + configs.LOADING_BAR_STEP)
        utils.assets.load_audios()
        self.loading_bar.set_value(self.loading_bar.value + configs.LOADING_BAR_STEP)
        utils.assets.load_fonts()
        self.loading_bar.set_value(self.loading_bar.value + configs.LOADING_BAR_STEP)
        self.ready = True

    def render(self):
        self.game.screen.fill(pygame.color.Color("white"))
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        if sys.platform == "emscripten":
            if self.ready:
                self.game.set_state(Start(self.game))
        else:
            if self.ready:
                self.thread.join()
                self.game.set_state(Start(self.game))
    
    def enter_state(self):
        if sys.platform == "emscripten":
            self.load_assets()
        else:
            self.thread = threading.Thread(target=self.load_assets)
            self.thread.start()
    
    def exit_state(self):
        self.game.fadein()