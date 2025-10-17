
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return 0
        random_angle = random.uniform(20,50)
        asteroid1_vector = self.velocity.rotate(random_angle)
        asteroid2_vector = self.velocity.rotate(-random_angle)
        self.radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_1.velocity = asteroid1_vector * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid_2.velocity = asteroid2_vector * 1.2

        return 100