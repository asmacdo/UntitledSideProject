import math


class Point:
    """
    A place on the field.
    """
    def __init__(self, x=0, y=0, z=0):
        """
        Defaults to center, on the ground.
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_point_on_line(self, slider=1):
        diff = self.p2 - self.p1
        return self.p2 + diff * (slider - 1)

    def angle_difference(self, ideal_line):
        ideal_angle = ideal_line.p1.ang_to(ideal_line.p2)
        my_angle = self.p1.ang_to(self.p2)
        return ideal_angle - my_angle

    def distance(self):
        dist = self.p2 - self.p1
        return dist.length()


# This is a helper class for vector math. You can extend it or delete if you want.
class Vec3:
    """
    This class should provide you with all the basic vector operations that you need, but feel free to extend its
    functionality when needed.
    The vectors found in the GameTickPacket will be flatbuffer vectors. Cast them to Vec3 like this:
    `car_location = Vec3(car.physics.location)`.

    Remember that the in-game axis are left-handed.

    When in doubt visit the wiki: https://github.com/RLBot/RLBot/wiki/Useful-Game-Values
    """

    def __init__(self, x: float , y: float=0, z: float=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @staticmethod
    def from_vec(other):
        return Vec3(other.x, other.y, other.z)

    def __getitem__(self, item: int):
        return (self.x, self.y, self.z)[item]

    def __add__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __mul__(self, scale: float) -> 'Vec3':
        return Vec3(self.x * scale, self.y * scale, self.z * scale)

    def __rmul__(self, scale):
        return self * scale

    def __truediv__(self, scale: float) -> 'Vec3':
        scale = 1 / float(scale)
        return self * scale

    def __str__(self):
        return "Vec3(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def flat(self):
        """Returns a new Vec3 that equals this Vec3 but projected onto the ground plane. I.e. where z=0."""
        return Vec3(self.x, self.y, 0)

    def length(self):
        """Returns the length of the vector. Also called magnitude and norm."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dist(self, other: 'Vec3') -> float:
        """Returns the distance between this vector and another vector using pythagoras."""
        return (self - other).length()

    def normalized(self):
        """Returns a vector with the same direction but a length of one."""
        return self / self.length()

    def rescale(self, new_len: float) -> 'Vec3':
        """Returns a vector with the same direction but a different length."""
        return new_len * self.normalized()

    def dot(self, other: 'Vec3') -> float:
        """Returns the dot product."""
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other: 'Vec3') -> 'Vec3':
        """Returns the cross product."""
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def ang_to(self, ideal: 'Vec3') -> float:
        """Returns the angle to the ideal vector. Angle will be between 0 and pi."""
        cos_ang = self.dot(ideal) / (self.length() * ideal.length())
        return math.acos(cos_ang)

    def offset(self, x=0, y=0, z=0):
        offset_vector = Vec3.from_vec(self)
        offset_vector.x += x
        offset_vector.y += y
        offset_vector.z += z
        return offset_vector

