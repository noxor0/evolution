import pygame

from commands.commander import Commander
from map.game_map import GameMap
from constants import game as gc


def main():
    pygame.init()
    pygame.mixer.quit()
    done = False
    screen = pygame.display.set_mode(gc.WINDOW_DIMENSIONS)
    clock = pygame.time.Clock()
    game_map = GameMap(screen)
    game_map.setup()
    game_map.draw()
    pygame.display.flip()

    commander = Commander(game_map)

    while not done:
        commander.execute_merp_commands()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        game_map.update()
        pygame.display.flip()
        clock.tick(15)


if __name__ == '__main__':
    main()
