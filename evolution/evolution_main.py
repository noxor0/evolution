import pygame
from map.game_map import GameMap
from constants import game as gc


def main():
    pygame.init()
    done = False
    screen = pygame.display.set_mode(gc.WINDOW_DIMENSIONS)
    clock = pygame.time.Clock()
    game_map = GameMap(screen)
    game_map.setup()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        game_map.draw()
        # game_map.update()
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
