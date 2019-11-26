from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from util.orientation import Orientation
from util.vec import Vec3

class State:

    def __init__(self, my_car_index):
        self.my_car_index = my_car_index

    def update(self, packet: GameTickPacket) -> SimpleControllerState:
        """
        """
        self.my_car = packet.game_cars[self.my_car_index]
        if self.my_car.team:
            direction = 1
        else: 
            direction = -1
        self.my_goal = Vec3(0.0, 5120 * direction, 0.0)
        self.target_goal = Vec3(0.0, 5120 * direction * -1, 0.0)
        self.ball_location = Vec3.from_vec(packet.game_ball.physics.location)
        self.car_location = Vec3.from_vec(self.my_car.physics.location)
        self.car_velocity = Vec3.from_vec(self.my_car.physics.velocity)
        self.car_to_ball = self.ball_location - self.car_location
        # TODO group these
        # Find the direction of our car using the Orientation class
        self.car_orientation = Orientation(self.my_car.physics.rotation)
        self.car_direction = self.car_orientation.forward
        self.impact_event = None


