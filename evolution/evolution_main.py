import pygame
import game_map
from constants import game as gc


def main():
    pygame.init()
    screen = pygame.display.set_mode(gc.WINDOW_DIMENSIONS)
    done = False
    map_ = game_map.GameMap(screen).setup_map()
    map_.setup_map()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()


if __name__ == '__main__':
    main()
