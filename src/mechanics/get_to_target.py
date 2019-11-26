import math

from util.radian import simplify_radian


def get_to_target(target, state, drawer, controller_state):

    steer_correction_radians = find_correction(target, state.car_direction, state.car_location)
    controller_state.throttle = 0.1
    controller_state.boost = False
    controller_state.handbrake = False

    print("get_to_target", "correction rad", steer_correction_radians)
    if abs(steer_correction_radians) > math.pi/ 2:
        controller_state.handbrake = True
        controller_state.throttle = 0.5
    elif abs(steer_correction_radians) < 1:
        # self.controller_state.throttle = 0.1
        controller_state.handbrake = False
        controller_state.throttle = 1.0
        controller_state.boost = True
    else:
        # self.controller_state.throttle = 1.0
        controller_state.handbrake = False

    if steer_correction_radians > 0:
        # Positive radians in the unit circle is a turn to the left.
        turn = -1.0  # Negative value for a turn to the left.
        drawer.chatter.append("turn left")
    else:
        turn = 1.0
        drawer.chatter.append("turn right")

    controller_state.steer = turn
    return controller_state

def find_correction(target, car_direction, car_location):
    """
    Finds the angle from current to ideal vector in the xy-plane. Angle will be between -pi and +pi.
    """
    # The in-game axes are left handed, so use -x
    relative_location = target.location - car_location
    current_in_radians = math.atan2(car_direction.y, -car_direction.x)
    ideal_in_radians = math.atan2(relative_location.y, -relative_location.x)

    return simplify_radian(ideal_in_radians - current_in_radians)
