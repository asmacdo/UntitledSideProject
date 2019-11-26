import pygame

from bot import UntitledSideProject
from drawer.pygame_drawer.packet import packet as ex_packet
from drawer.pygame import Drawer as PygameDrawer
from drawer.pygame import GAME_DIMENSIONS, Location
from rlbot.utils.structures.game_data_struct import GameTickPacket

def main():
    me = UntitledSideProject("hello", "blue", 0)
    # packet = GameTickPacket(ex_packet)
    pygame_drawer = PygameDrawer()

    target = Location()
    me = Location(0, 100, 0)
    # pygame_drawer.draw_circle(location)
    pygame_drawer.draw_path(me, target)
    pygame_drawer.draw_target(target)
    pygame_drawer.draw_my_car(me)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
if __name__ == "__main__":
    main()
