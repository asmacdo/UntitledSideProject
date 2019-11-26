from strategy import DriveAtBall, DriveAtCenter, DriveBehindBall, DriveAtMyGoal
from util.vec import Line, Vec3

def select_strategy(state, D, P):
    # self.S.target_goal = Vec3(0.0, 5125.0, 0.0)
    car_to_target = Line(state.car_location, state.target_goal)
    D.draw_line(car_to_target)
    ball_to_target = Line(state.ball_location, state.target_goal)
    D.draw_line(ball_to_target)

    if car_to_target.distance() > ball_to_target.distance():
    # if car_to_target.distance() < ball_to_target.distance():
        # return DriveAt
        # return DriveAtBall(state, D)
        return DriveAtBall(state, D)
    else:
        return DriveAtMyGoal(state, D)
    # return DriveBehindBall(state, drawer)
