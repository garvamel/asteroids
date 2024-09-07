import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            v_1 = self.velocity.rotate(angle)
            v_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astrd_1 = Asteroid(self.position.x, self.position.y, new_radius)
            astrd_1.velocity = v_1 *1.2
            astrd_2 = Asteroid(self.position.x, self.position.y, new_radius)
            astrd_2.velocity = v_2 *1.2


