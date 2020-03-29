from sys import exit

import pygame


class Player():

    def __init__(self, screen, image_name):
        self.screen = screen
        self.image = pygame.transform.scale(
                pygame.image.load(image_name).convert_alpha(), (100,100)
                )
        self.rect = self.image.get_rect()

        self.rect.bottom = self.screen.get_rect().bottom
        self.rect.centerx = self.screen.get_rect().centerx

    def draw(self):
        self.screen.blit(self.image, self.rect)


def run_game():

    pygame.init()
    screen = pygame.display.set_mode(( 1000, 1000 ))
    pygame.display.set_caption('MINECRAFT MY LIFE')

    bg_color = (139, 228, 223)
    sonic = Player(screen, 'bird.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        screen.fill(bg_color)
        sonic.draw()
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
