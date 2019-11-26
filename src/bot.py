import math
import time

from drawer import Drawer
# from mechanics.get_to_target import get_to_target
from mechanics.slow_drive import get_to_target
from state import State
from strategy.select_strat import select_strategy
from drawer.pygame import Drawer as PygameDrawer
from drawer.pygame import Location

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket


class UntitledSideProject(BaseAgent):

    def initialize_agent(self):
        """
        Callback from BaseAgent.__init__()
        TODO does this nested class affect performance?
        """
        # TODO self.initialize_log()
        self.controller_state = SimpleControllerState()
        self.S = State(self.index)
        self.D = Drawer(self.renderer)
        self.P = PygameDrawer()
        self.strategy = None

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        """
        Recieves: 1/60 second of new game information
        Returns: what buttons to push
        """
        print("FRAME")
        self.D._start_frame()
        self.P._start_frame()
        self.S.update(packet)

        strategy = select_strategy(self.S, self.D, self.P)
        ball_prediction = self.get_ball_prediction_struct()
        # print(ball_prediction)
        target = strategy.calculate_target(ball_prediction)

        # pygame_drawer.draw_circle(location)
        # print("Car location", self.S.car_location)
        if self.S.impact_event is not None:
            self.P.draw_target(self.S.impact_event["predicted_ball_location"])
        self.P.draw_path(self.S.car_location, target.location)
        self.P.draw_my_car(self.S.ball_location, color=(255, 0, 255))
        self.P.draw_my_car(self.S.car_location)
        # print(packet)

        buttons_to_push = get_to_target(target, self.S, self.D, self.controller_state)
        self.D._finish_frame()
        self.P._finish_frame()
        return buttons_to_push

