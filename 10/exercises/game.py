import random

import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT,
                            MOUSEBUTTONDOWN)

from colors import *

# Dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000

class Player(pygame.sprite.Sprite):

    def __init__(self, width: int, height: int, color: tuple, step: int):
        super().__init__()
        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.step = step

    def update_color(self):
        self.surface.fill(random.choice(COLORS))

    def update_position(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.step, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.step, 0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.step)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.step)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


def main():
    # Подготовить pygame к работе.
    pygame.init()
    # Устанавливаем широту и высоту экрана.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Устанавливаем название игры.
    pygame.display.set_caption('MINECRAFT MY LIFE')
    # Create player
    player1 = Player(50, 50, BLUE, 5)  # width, height, color, step
    # Запускаем игровой цикл
    while True:
        for event in pygame.event.get():
            # Если нажал на закрыть окно (Х)
            if event.type == QUIT:
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # if left mouse
                    x, y = event.pos
                    if player1.rect.collidepoint(x, y):
                        player1.update_color()

        # If pressed keys -> move position
        player1.update_position()
        # If clicked by mouse -> change color
        # player1.update_color()
        # Задний фон отрисовать
        screen.fill(SKY_BLUE)
        # Draw player (sprite)
        screen.blit(player1.surface, player1.rect)
        # Обновить экран
        pygame.display.flip()


if __name__ == '__main__':
    main()
