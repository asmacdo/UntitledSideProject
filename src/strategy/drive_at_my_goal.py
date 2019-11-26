import math

from target import Target
from util.vec import Line, Vec3

from strategy.base import Strategy

class DriveAtMyGoal(Strategy):

    def calculate_target(self, _):
        car_to_target = Line(self.S.my_goal, self.S.car_location)
        self.D.draw_line(car_to_target, color="orange")

        distance = car_to_target.distance()
        print("Distance to target: ", distance)
        # if distance < 200:
        #     return Target(location=self.S.car_location)
        return Target(location=self.S.my_goal)


