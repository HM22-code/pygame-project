import pygame.sprite
import random
import assets
import configs
from layer import Layer

class Particle(pygame.sprite.Sprite):
    
    # a particle is...
    # a thing that exists at a location
    # typically moves around
    # typically changes over time
    # and typically disappears after a certain amount of time
    
    # [loc, velocity, timer]
    particles = []
    color = (255, 255, 255)
    
    def __init__(self, x, y, width, height,*groups):
        self._layer = Layer.PLAYER
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        super().__init__(*groups)
        
    def update(self):
        self.particles.append([[self.rect.x, self.rect.y], [random.randint(0,20) / 10 - 1, -2], random.randint(4,6)])
        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            pygame.draw.circle(self.rect, self.color, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)