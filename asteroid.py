import random
from logger import log_event
from player import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.__radius = radius
        pass

    def draw(self,screen):
        # points = self.triangle()
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,30)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            mini_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            mini_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            mini_asteroid1.velocity = new_vector1 * 1.2
            mini_asteroid2.velocity = new_vector2 * 1.2
