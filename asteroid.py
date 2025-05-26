import pygame, constants, circleshape, random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        
        random_angle = random.uniform(20, 50)

        asteroid1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        asteroid2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))

        asteroid1.velocity = self.velocity.rotate(random_angle)*SPLIT_ASTEROID_INCREASE
        asteroid2.velocity = self.velocity.rotate(-random_angle)*SPLIT_ASTEROID_INCREASE

        self.kill()