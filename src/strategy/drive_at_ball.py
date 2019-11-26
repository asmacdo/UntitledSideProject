import math

from target import Target
from util.vec import Line, Vec3

from strategy.base import Strategy

class DriveAtBall(Strategy):

    def calculate_target(self, ball_prediction):

        # goal= Vec3(0.0, 5120.0, 0.0)
        # ball_to_target = Line(goal, self.S.ball_location)
        # car_to_ball = Line(self.S.car_location, self.S.ball_location)
        # hit_prep = ball_to_target.get_point_on_line(1.2)
        # car_to_hit_prep = Line(self.S.car_location, hit_prep)
        #
        # ideal_orientation = 

        # if car_to_hit_prep is not mostly straight, target hit prep
        # angle_diff = abs(ball_to_target.angle_difference(car_to_hit_prep))
        # print(angle_diff)
        # if angle_diff < 2:
        #     print("GOFORIT")
        #     self.go = True
        # else:
        #     planned_location = hit_prep
        #     self.go = False
        #     print("not yet")
        #
        plan = Line(self.S.car_location, self.S.ball_location)
        # TODO make sure this is at least kind of close
        slices_to_impact = int(plan.distance() / (self.S.car_velocity.length() / 60)) 
        # print("TO BALL", plan.distance())
        # print("Speed", self.S.car_velocity.length())

        if slices_to_impact > len(ball_prediction.slices):
            # print("BALLCHASING")
            predicted_location = self.S.ball_location
        else:
            # print("smart********************************")
            # print("Slices to impact", slices_to_impact)
            # print(slices_to_impact)
            predicted_location = ball_prediction.slices[slices_to_impact].physics.location
            self.S.impact_event = {
                "slices": slices_to_impact,
                "predicted_ball_location": predicted_location}
            self.D.draw_line(plan, color="orange")

        if slices_to_impact < 1:
            self.S.impact_evenct = None
        # self.D.draw_line(ball_to_target)
        return Target(location=predicted_location)


