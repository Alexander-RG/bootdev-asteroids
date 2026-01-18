from player import CircleShape
from constants import LINE_WIDTH
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
