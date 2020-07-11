import sys
import pygame

class Snake:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.reset_snake()

    def reset_snake(self):
        self.parts = []
        self.size = 1

        self.side = self.settings.cube_side
        self.head_x = self.screen_rect.centerx
        self.head_y = self.screen_rect.centery
        self.head_rect = pygame.Rect(self.head_x, self.head_y, self.side, self.side)

        self.prev_head_x = 0
        self.prev_head_y = 0

        self.direction = ''

    def update_head(self):
        self.prev_head_x = self.head_x
        self.prev_head_y = self.head_y
        if self.direction == 'up':
            if self.head_rect.top == self.screen_rect.top:
                self.head_y = self.screen_rect.bottom - self.side
            else:
                self.head_y -= self.side
        elif self.direction == 'down':
            if self.head_rect.bottom == self.screen_rect.bottom:
                self.head_y = self.screen_rect.top
            else:
                self.head_y += self.side
        elif self.direction == 'left':
            if self.head_rect.left == self.screen_rect.left:
                self.head_x = self.screen_rect.right - self.side
            else:
                self.head_x -= self.side
        elif self.direction == 'right':
            if self.head_rect.right == self.screen_rect.right:
                self.head_x = self.screen_rect.left
            else:
                self.head_x += self.side
        self.head_rect.x = self.head_x
        self.head_rect.y = self.head_y

    def update_body_parts(self):
        if self.parts:
            # Update the first body_part which follows the head
            self.parts[0].update(self.prev_head_x, self.prev_head_y)
            for i in range(1, len(self.parts)):
                # Update every other part of the body which follows the previous part
                self.parts[i].update(self.parts[i - 1].prev_x, self.parts[i - 1].prev_y)

    def update_snake(self, apple):
        self.update_head()
        self.update_body_parts()
        self.check_collision()
        self.check_eat_apple(apple)

    def add_part(self):
        self.size += 1
        part = Part(self, self.settings, self.screen)
        self.parts.append(part)

    def check_collision(self):
        if self.parts:
            for part in self.parts:
                if self.head_rect.colliderect(part.rect):
                    print(f"You got a snake of size: {self.size}!")
                    self.reset_snake()

    def check_eat_apple(self, apple):
        if self.head_rect.colliderect(apple.rect):
            snake_coords = self.get_snake_coords()
            map_coords = self.settings.get_map_coord()
            for coord in snake_coords:
                map_coords.remove(coord)
            apple.update(apple.find_apple_spot(self.get_snake_coords()))
            self.add_part()

    # Get coordonates of every part of the snake
    def get_snake_coords(self):
        snake_coords = []
        snake_coords.append((self.head_x, self.head_y))
        for part in self.parts:
            snake_coords.append((part.x, part.y))
        return snake_coords

    def draw(self):
        # Draw head
        pygame.draw.rect(self.screen, self.settings.head_color, (self.head_x, self.head_y, self.side, self.side))
        for part in self.parts:
            part.draw()

class Part:
    def __init__(self, snake, settings, screen):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.side = self.settings.cube_side
        self.x = snake.prev_head_x
        self.y = snake.prev_head_y
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)

        self.prev_x = 0
        self.prev_y = 0

    def update(self, x, y):
        # Position
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = x
        self.y = y

        # Update rectangle
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.part_color, (self.x, self.y, self.side, self.side))