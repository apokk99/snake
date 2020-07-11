import sys

try:
    import pygame
except:
    print('You must install pygame')

from settings import Settings
from snake import Snake
from apple import Apple

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")

        self.snake = Snake(self.settings, self.screen)
        self.apple = Apple(self.settings, self.screen)

    def run_game(self):
        while True:
            pygame.time.delay(80)
            self._check_events()

            self.snake.update_snake(self.apple)
            self.check_win_condition()

            self._update_screen()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                break

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        # for every move choice (up, down, left right) snake can't go backwards unless there is only the head
        elif event.key == pygame.K_UP and (self.snake.direction != 'down' or self.snake.size == 1):
            self.snake.direction = 'up'
        elif event.key == pygame.K_DOWN and (self.snake.direction != 'up' or self.snake.size == 1):
            self.snake.direction = 'down'
        elif event.key == pygame.K_LEFT and (self.snake.direction != 'right' or self.snake.size == 1):
            self.snake.direction = 'left'
        elif event.key == pygame.K_RIGHT and (self.snake.direction != 'left' or self.snake.size == 1):
            self.snake.direction = 'right'

    def check_win_condition(self):
        if self.snake.size == self.settings.total_cubes:
            print(f"You have won! Snake size: {self.snake.size}")
            sys.exit()

    def draw_grid(self):
        for x in range(0, self.settings.screen_width, self.settings.cube_side):
            pygame.draw.line(self.screen, self.settings.grid_color, (x, 0), (x, self.settings.screen_height))
        for y in range(0, self.settings.screen_height, self.settings.cube_side):
            pygame.draw.line(self.screen, self.settings.grid_color, (0, y), (self.settings.screen_width, y))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.snake.draw()
        self.apple.draw()
        self.draw_grid()

if __name__ == "__main__":
    ai = SnakeGame()
    ai.run_game()