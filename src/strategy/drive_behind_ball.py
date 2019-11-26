import math

from target import Target
from util.vec import Line, Vec3

from strategy.base import Strategy

class DriveBehindBall(Strategy):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.checkpoints = []

    def calculate_target(self):
        if not self.checkpoints:
            self.calculate_checkpoints()

    def calculate_checkpoints(self):
        goal = Vec3(0.0, 5125.0, 0.0)
        ball_to_target = Line(goal, self.S.ball_location)
        self.D.draw_line(ball_to_target)

        car_to_ball = Line(self.S.car_location, self.S.ball_location)
        self.D.draw_line(car_to_ball)

        hit_prep = ball_to_target.get_point_on_line(1.2)
        hit_prep.z = 0
        car_to_hit_prep = Line(self.S.car_location, hit_prep)
        target = Target(location=hit_prep)
        self.checkpoints.append(target)
        ball = Target(location=self.S.ball_location)
        self.checkpoints.append(target)
        print([check.location for check in self.checkpoints])

        # if car_to_hit_prep is not mostly straight, target hit prep
        # angle_diff = abs(ball_to_target.angle_difference(car_to_hit_prep))
        # print(angle_diff)
        # if angle_diff < 2:
        #     print("GOFORIT")
        #     self.go = True
        #     planned_location = self.S.ball_location
        # else:
        planned_location = hit_prep
        #     self.go = False
        #     print("not yet")
        #
        # plan = Line(self.S.car_location, planned_location)
        # self.D.draw_line(plan, color="orange")
        return Target(location=planned_location)


