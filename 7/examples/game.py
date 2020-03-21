import pygame

from pygame.locals import (
        RLEACCEL,
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
)

pygame.init()

GAME_NAME = 'My First Python Game'

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 800

PLAYER_WIDTH  = 100
PLAYER_HEIGHT = 100
PLAYER_SPEED  = 1
PLAYER_IMAGE  = 'angry-bird.png'

BLUE   = (0, 0, 255)
CYAN   = (0, 255, 255)
GREEN  = (0, 255, 0)
GREY   = (204, 204, 255)
ORANGE = (255, 102, 0)
PINK   = (255, 0, 255)
PURPLE = (102, 0, 102)
RED    = (255, 0, 0)
SKY_BLUE = (207, 240, 244)
WHITE  = (255, 255, 255)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.surface = pygame.transform.scale(self.surface,
                                              (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.surface.set_colorkey(WHITE, RLEACCEL)
        self.rect = self.surface.get_rect()

    def update(self, pressed_keys):
        # Move player on the screen
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -PLAYER_SPEED)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, PLAYER_SPEED)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)

        # Keep player on the screeen.
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Create window.
screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
pygame.display.set_caption(GAME_NAME)

# Create player.
player = Player()

run = True
while run:

    for event in pygame.event.get():

        # If pressed any key
        if event.type == KEYDOWN:
            # If pressed <Escape>
            if event.key == K_ESCAPE:
                run = False

        # If Clicked 'X'
        if event.type == pygame.QUIT:
            run = False

    # Set main screen backgrond color.
    screen.fill(SKY_BLUE)

    # Update player's position.
    player.update(pygame.key.get_pressed())

    # Draw Player
    screen.blit(player.surface, player.rect)

    # Update the screen
    pygame.display.flip()

pygame.quit()
