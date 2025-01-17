from objects.background import Background
from objects.text import Text
from interfaces.state import State
import utils.assets
import pygame
import configs
import sys

class Ending(State):
    """ Ending state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.sprites.add(Background())
        self.upper_font = "retro.ttf"
        self.lower_font = "score.ttf"
        self.created_text = Text(configs.SCREEN_WIDTH // 2 - 50, configs.SCREEN_HEIGHT // 6, "Created by", self.upper_font, 20, pygame.color.Color("white"))
        self.creator_text = Text(configs.SCREEN_WIDTH // 2 - 40, configs.SCREEN_HEIGHT // 3.8, "jude erdrick", self.lower_font, 10, pygame.color.Color("white"))
        self.graphics_text = Text(configs.SCREEN_WIDTH // 2 - 40, configs.SCREEN_HEIGHT // 2.2, "Graphics", self.upper_font, 20, pygame.color.Color("white"))
        self.graphic_text = Text(configs.SCREEN_WIDTH // 2 - 25, configs.SCREEN_HEIGHT // 1.8, "ansimuz", self.lower_font, 10, pygame.color.Color("white"))
        self.musics_text = Text(configs.SCREEN_WIDTH // 2 - 75, configs.SCREEN_HEIGHT // 1.4, "Musics & sounds", self.upper_font, 20, pygame.color.Color("white"))
        self.music_text = Text(configs.SCREEN_WIDTH // 2 - 35, configs.SCREEN_HEIGHT // 1.22, "juhani junkala", self.lower_font, 10, pygame.color.Color("white"))
        self.sprites.add(self.created_text)
        self.sprites.add(self.creator_text)
        self.sprites.add(self.graphics_text)
        self.sprites.add(self.graphic_text)
        self.sprites.add(self.musics_text)
        self.sprites.add(self.music_text)
        # Background music
        if sys.platform == "emscripten":
            self.music = utils.assets.get_audio("ending.ogg")
        else:
            self.music = utils.assets.get_audio("ending.wav")
    
    def render(self):
        self.sprites.draw(self.game.screen)
    
    def update(self, dt):
        self.sprites.update(dt)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.previous_state)
        
    def enter_state(self):
        self.music.set_volume(self.game.music_volume)
        self.music.play(loops = -1)
        pygame.mouse.set_visible(False)
    
    def exit_state(self):
        self.music.stop()
        pygame.mouse.set_visible(True)