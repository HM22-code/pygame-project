import pygame
import utils.assets
import configs
from objects.button import Button
from states.ending import Ending
from objects.background import Background
from objects.title import Title
from interfaces.state import State
from states.menu import Menu
from states.option import Option

class Start(State):
    """ Start state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        self.sprites.add(Background())
        self.sprites.add(Title())
        # Adding buttons
        self.buttons = []
        self.create_buttons()
        # Background music
        self.game.music = utils.assets.get_audio("menu")
        
    def start(self):
        self.game.set_state(Menu(self.game))
    
    def options(self):
        self.game.set_state(Option(self.game))
    
    def credits(self):
        self.game.set_state(Ending(self.game))
    
    def quit(self):
        self.game.quit()
        
    def create_buttons(self):
        """ Create buttons objects
        """
        menu_items = [
            {
                'title' : 'Start',
                'action' : lambda: self.start(),
            },
            {
                'title' : 'Options',
                'action' : lambda: self.options(),
            },
            {
                'title' : 'Credits',
                'action' : lambda: self.credits(),
            },
            {
                'title' : 'Quit',
                'action' : lambda: self.quit(),
            }
        ]
        button_total_height = len(menu_items) * (configs.BUTTON_HEIGHT + configs.BUTTON_SPACING)
        starting_x = (configs.SCREEN_WIDTH - configs.BUTTON_WIDTH) // 2
        starting_y = (configs.SCREEN_HEIGHT - button_total_height) // 2
        for item in menu_items:
            button = Button(starting_x, starting_y, configs.BUTTON_WIDTH, configs.BUTTON_HEIGHT, item["title"], item["action"])
            starting_y += configs.BUTTON_HEIGHT + configs.BUTTON_SPACING
            self.sprites.add(button)
            self.buttons.append(button)
    
    def run(self):
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
        
    def handle_event(self, event):
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.action()
        
    def enter_state(self):
        self.game.music.set_volume(self.game.music_volume)
        self.game.music.play(loops = -1)
    
    def exit_state(self):
        self.game.music.fadeout(1000)
        self.game.fadein()
        
    def process_input(self):
        super().process_input()
    
    def render(self):
        super().render()
    
    def update(self):
        super().update()