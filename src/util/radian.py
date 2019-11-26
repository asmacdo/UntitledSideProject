import math

def simplify_radian(rad):
    # Make sure that diff is between -pi and +pi.
    if abs(rad) > math.pi:
        if rad < 0:
            rad += 2 * math.pi
        else:
            rad -= 2 * math.pi
    return rad



