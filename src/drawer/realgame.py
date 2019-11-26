class Drawer:
    def __init__(self, renderer=None):
        if renderer is not None:
            self.renderer = renderer

    def _start_frame(self):
        self.chatter = []
        self.renderer.begin_rendering()

    def _finish_frame(self):
        # self._display_chatter()
        self.renderer.end_rendering()

    # def _display_chatter(self):
    #     # print the action that the bot is taking
    #     text_block = "\n".join(self.chatter)
    #     self.renderer.draw_string_3d(
    #         self.S.my_car.physics.location,
    #         2, # TODO WHATSTHIS
    #         2, # TODO WHATSTHIS
    #         text_block,
    #         self.renderer.white()
    #     )

    def draw_line(self, line, color=None):
        if color is None:
            color = self.renderer.red()
        else:
            color = self.renderer.orange()
        self.renderer.draw_line_3d(
            line.p1,
            line.p2,
            color
        )

    def render_target(self, target):
        print("RENDERING TARGET")
        print(type(self.renderer))
        self.renderer.draw_rect_3d(target.location, 20, 20, True, self.renderer.red(), centered=True)
            # def draw_rect_3d(self, vec, width, height, filled, color, centered=False):

    def render_checkpoints(self, checkpoints):
        for target in checkpoints:
            self.render_target(target)

    # def line_from_car_to_ball(self):
    #     # draw a line from the car to the ball
    #     self.renderer.draw_line_3d(
    #         self.S.my_car.physics.location,
    #         self.S.ball_location,
    #         self.renderer.white()
    #     )
    # def line_from_ball_to_target(self, target_vector):
    #     # draw a line from the car to the ball
    #     self.renderer.draw_line_3d(
    #         self.S.ball_location,
    #         target_vector,
    #         self.renderer.white()
    #     )
