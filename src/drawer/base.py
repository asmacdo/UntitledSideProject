class Drawer:
    def __init__(self):
        pass

    def start_frame(self):
        pass

    def finish_frame(self):
        pass

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
