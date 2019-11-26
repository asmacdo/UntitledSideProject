from util.vec import Line, Vec3

class Target:
    def __init__(self, location=None, orientation=None):
        if location is None:
            self.location = None
        else:
            self.location = Vec3.from_vec(location)

        if orientation is None:
            self.orientation = None
        else:
            self.orientation = Vec3.from_vec(orientation)



