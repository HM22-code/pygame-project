import pygame
import configs.button
import configs.screen
from classes.state import State
from objects.background import Background
from objects.button import Button
from objects.title import Title
from states.level1 import Level1
from states.level2 import Level2
from states.level3 import Level3

class Menu(State):
    """ Menu state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        Background(self.sprites)
        Title(self.sprites)
        # Adding buttons
        self.buttons = []
        self.create_buttons()
        
    def level1(self):
        self.game.set_state(Level1(self.game))
    
    def level2(self):
        self.game.set_state(Level2(self.game))
    
    def level3(self):
        self.game.set_state(Level3(self.game))
    
    def create_buttons(self):
        """ Create buttons objects
        """
        menu_items = [
            {
                'title' : 'Level 1',
                'action' : lambda: self.level1(),
            },
            {
                'title' : 'Level 2',
                'action' : lambda: self.level2(),
            },
            {
                'title' : 'Level 3',
                'action' : lambda: self.level3(),
            }
        ]
        button_total_height = len(menu_items) * (configs.button.BUTTON_HEIGHT + configs.button.BUTTON_SPACING)
        starting_x = (configs.screen.SCREEN_WIDTH - configs.button.BUTTON_WIDTH) // 2
        starting_y = (configs.screen.SCREEN_HEIGHT - button_total_height) // 2
        for item in menu_items:
            button = Button(starting_x, starting_y, configs.button.BUTTON_WIDTH, configs.button.BUTTON_HEIGHT, item["title"], item["action"], self.sprites)
            starting_y += configs.button.BUTTON_HEIGHT + configs.button.BUTTON_SPACING
            self.buttons.append(button)
            
    def run(self):
        # Draw
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()
    
    def handle_event(self, event):
        mx, my = pygame.mouse.get_pos()
        for button in self.buttons:
            # Check if hover
            if button.rect.collidepoint((mx, my)):
                button.active = True
                # Check if click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.action()
            else: 
                button.active = False
            
        
    