import math

from target import Target
from util.vec import Line, Vec3

from strategy.base import Strategy

class DriveAtCenter(Strategy):

    def calculate_target(self):
        center = Vec3(0.0, 0.0, 0.0)
        goal = Vec3(0.0, 5120, 0.0)
        car_to_target = Line(center, self.S.car_location)
        center_to_goal = Line(center, goal)
        self.D.draw_line(car_to_target, color="orange")
        self.D.draw_line(center_to_goal)

        distance = car_to_target.distance()
        print("Distance to target: ", distance)
        # if distance < 200:
        #     return Target(location=self.S.car_location)
        return Target(location=center)


