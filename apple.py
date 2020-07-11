import random

import pygame

class Apple:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.side = self.settings.cube_side
        self.x = random.randrange(0, self.settings.screen_width, self.settings.cube_side)
        self.y = random.randrange(0, self.settings.screen_height, self.settings.cube_side)
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)

    def find_apple_spot(self, snake_coords):
        map_coords = self.settings.get_map_coord()
        for coord in snake_coords:
            map_coords.remove(coord)
        return random.choice(map_coords)

    def update(self, coord):
        self.x = coord[0]
        self.y = coord[1]

        # Update rect position
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.apple_color, (self.x, self.y, self.side, self.side))