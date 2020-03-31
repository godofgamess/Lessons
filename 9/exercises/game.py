import pygame

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT)


# Colors
SKY_BLUE = 139, 228, 223
RED      = 255, 0, 0
MAROON   = 128, 0, 0
LIME     = 0, 255, 0
GREEN    = 0, 128, 0
BLUE     = 0, 0, 255
NAVY     = 0, 0, 128
YELLOW   = 255, 255, 0
MAGENTA  = 255, 0, 255
PURPLE   = 128, 0, 128
BLACK    = 0, 0, 0
WHITE    = 255, 255, 255
GRAY     = 128, 128, 128
CYAN     = 0, 255, 255
# Dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
CIRCLE_RADIUS = 50
RECT_WIDTH  = CIRCLE_RADIUS * 2
RECT_HEIGHT = CIRCLE_RADIUS * 2

def main():
    # Подготовить pygame к работе.
    pygame.init()
    # Устанавливаем широту и высоту экрана.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Устанавливаем название игры.
    pygame.display.set_caption('MINECRAFT MY LIFE')
    # Цвет заднего фона.
    # Запускаем игровой цикл
    while True:
        for event in pygame.event.get():
            # Если нажал на закрыть окно (Х)
            if event.type == QUIT:
                pygame.quit()

        # Задний фон отрисовать
        screen.fill(SKY_BLUE)
        # Where, Color, Center Pos, Radius
        pygame.draw.circle(screen, RED, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10), CIRCLE_RADIUS)
        pygame.draw.circle(screen, LIME, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10), CIRCLE_RADIUS)
        pygame.draw.circle(screen, BLUE, (SCREEN_WIDTH // 10 * 9, SCREEN_HEIGHT // 10), CIRCLE_RADIUS)
        pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10 * 9), CIRCLE_RADIUS)
        pygame.draw.circle(screen, MAGENTA, (SCREEN_WIDTH // 10 * 9 , SCREEN_HEIGHT // 10 * 9), CIRCLE_RADIUS)
        pygame.draw.circle(screen, BLACK, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 2), CIRCLE_RADIUS)
        pygame.draw.circle(screen, WHITE, (SCREEN_WIDTH // 10 * 9, SCREEN_HEIGHT // 2), CIRCLE_RADIUS)
        pygame.draw.circle(screen, CYAN, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10 * 9), CIRCLE_RADIUS)

        pygame.draw.rect(screen, GRAY, ((SCREEN_WIDTH  // 2 - CIRCLE_RADIUS, SCREEN_HEIGHT // 2 - CIRCLE_RADIUS),
                                        (RECT_WIDTH, RECT_HEIGHT)))
        pygame.draw.rect(screen, PURPLE, ((SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4), (RECT_WIDTH, RECT_HEIGHT)))
        pygame.draw.rect(screen, GREEN, ((SCREEN_WIDTH//4*3 - 2*CIRCLE_RADIUS, SCREEN_HEIGHT//4*3 - 2*CIRCLE_RADIUS),
                                        (RECT_WIDTH, RECT_HEIGHT)))

        pygame.draw.rect(screen, NAVY, ((SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4 * 3 - 2*CIRCLE_RADIUS), (RECT_WIDTH, RECT_HEIGHT)))
        pygame.draw.rect(screen, MAROON, ((SCREEN_WIDTH //4*3 - 2*CIRCLE_RADIUS, SCREEN_HEIGHT //4), (RECT_WIDTH, RECT_HEIGHT)))
        # Обновить экран
        pygame.display.flip()


if __name__ == '__main__':
    main()
