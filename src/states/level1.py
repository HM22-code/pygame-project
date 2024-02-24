import pygame
import utils.assets
from objects.player import Player
from objects.background import Background
from interfaces.state import State

class Level1(State):
    """ Level state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.sprites.add(Background())
        self.sprites.add(Player())
        # Background music
        self.game.music = utils.assets.get_audio("level1")
    
    def run(self):
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.set_state(self.game.get_previous_state())
        
    def enter_state(self):
        self.game.music.set_volume(self.game.music_volume)
        self.game.music.play(loops = -1)
    
    def exit_state(self):
        self.game.music.stop()
        
    def process_input(self):
        super().process_input()
    
    def render(self):
        super().render()
    
    def update(self):
        super().update()