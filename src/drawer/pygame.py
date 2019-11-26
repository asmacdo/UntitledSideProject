import pygame


PYGAME_SCALE = 0.1

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()


class GAME_DIMENSIONS:
    WIDTH = 8192.0
    HEIGHT = 10240.0

    @classmethod
    def convert_to_window(cls, scale=None):
        if scale is None:
            scale=PYGAME_SCALE
        return (
            int(cls.WIDTH * scale),
            int(cls.HEIGHT * scale)
        )

class Location:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


    def to_rocket_league(self):
        return (
            int(x - (GAME_DIMENSIONS.WIDTH / 2)),
            int(y - (GAME_DIMENSIONS.HEIGHT/ 2)),
            self.z
        )

    @classmethod
    def from_rl(cls, location):
        x = int((location.x + (GAME_DIMENSIONS.WIDTH / 2)) * PYGAME_SCALE)
        y = int((location.y + (GAME_DIMENSIONS.HEIGHT/ 2)) * PYGAME_SCALE)
        z = location.z
        return Location(x, y, z)


class Drawer:
    def __init__(self, screen=None, dimensions=None):
        if screen is None:
            self.screen = pygame.display.set_mode(GAME_DIMENSIONS.convert_to_window())


        if dimensions is not None:
            self.dimensions = dimensions
        self.background_colour = (150,150, 150)

    def _start_frame(self):
        self.screen.fill(self.background_colour)
    #
    def _finish_frame(self):
        pygame.display.flip()
    #     self.renderer.end_rendering()
    #
    def draw_my_car(self, rl_location, color=None):
        print("MY RL LOCATION", rl_location)
        location = Location.from_rl(rl_location)
        print("draw circle at:", location.x, location.y)
        pygame.draw.circle(self.screen, (0,0,255), (location.x, location.y), 15, 1)

    def draw_target(self, rl_location, color=None):
        if color is None:
            red = (255, 0, 0)
        location = Location.from_rl(rl_location)
        start = (location.x + 10, location.y + 10)
        end = (location.x - 10, location.y - 10)
        self.draw_line(start, end)
        start = (location.x - 10, location.y + 10)
        end = (location.x + 10, location.y - 10)
        self.draw_line(start, end)

    def draw_path(self, rl_current, rl_target):
        current = Location.from_rl(rl_current)
        target = Location.from_rl(rl_target)
        self.draw_line((current.x, current.y), (target.x, target.y), color=(255, 255, 100))

    def draw_line(self, start, end, color=None):
        if color is None:
            red = (255, 0, 0)
            color = red
        pygame.draw.line(self.screen, color, start, end, 5)


    def _draw_line(self, line, color=None):
        raise NotImplementedError()

    def _render_ball(self, ball_location):
        raise NotImplementedError()

    def _render_car(self, car_hitbox, car_location, car_orientation):
        raise NotImplementedError()

    def _render_target(self, target):
        raise NotImplementedError()

    def _render_checkpoints(self, checkpoints):
        for target in checkpoints:
            self.render_target(target)
