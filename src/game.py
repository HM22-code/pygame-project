import pygame
import configs
import assets
import sys
from states.start import Start

class Game:
    """ Game class
    """
    
    def __init__(self):
        # Init game running
        self.running = True
        # Initialize Pygame
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        # Loading assets
        assets.load_sprites()
        assets.load_audios()
        # Screen options
        pygame.display.set_icon(assets.get_sprite("icon"))
        pygame.display.set_caption(configs.TITLE)
        # Clock to control FPS
        self.clock = pygame.time.Clock()
        # Init Game state manager
        self.init_state()
        
    def init_state(self):
        """ Init state
        """
        self.current_state = Start(self)
        self.current_state.enter_state()
        self.previous_state = None
        
    def get_current_state(self):
        """ Get current state

        Returns:
            _type_: state
        """
        return self.current_state
    
    def get_previous_state(self):
        """ Get previous state

        Returns:
            _type_: state
        """
        return self.previous_state
    
    def set_state(self, state):
        """ Change the current state

        Args:
            state (_type_): state
        """
        self.previous_state = self.current_state
        self.previous_state.exit_state()
        self.current_state = state
        self.current_state.enter_state()
    
    def process_input(self):
        """ Process input event
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            # Current state event handling
            self.get_current_state().handle_event(event)
    
    def update(self):
        """ Current state update
        """
        self.get_current_state().run()
    
    def render(self):
        """ Update the full display Surface to the screen
        """
        pygame.display.flip()
    
    def run(self):
        """ Game loop
        """
        while self.running:
            self.process_input()
            self.update()
            self.render()
            # Limits FPS to 60
            self.clock.tick(configs.FPS)
            
    def quit(self):
        """ Quit game program
        """
        self.running = False
        pygame.quit()
        sys.exit()
        
Game().run()
        
