import pygame

import tile_constants as tc

WINDOW_SIZE = (800, 800)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    done = False

    while not done:
        create_tile(screen, 30, 30, tile_type='dirt')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()


def create_tile(screen, x, y, tile_type='dirt'):
    tile = tc.TILES.get(tile_type)
    pygame.draw.rect(screen, tile.get(tc.FILL_COLOR), pygame.Rect(x, y, tc.TILE_SIZE, tc.TILE_SIZE))
    pygame.draw.rect(screen, tile.get(tc.OUTLINE_COLOR), pygame.Rect(x, y, tc.TILE_SIZE, tc.TILE_SIZE), tc.TILE_OUTLINE)


if __name__ == '__main__':
    main()
