import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logic.controller import Controller


class Game:
    current_turn = {
        "turn_count": 0,
        "attacker": None,
        "target": None,
    }

    def __init__(self, controller):
        self.controller: Controller = controller

    def shuffle_players(self):
        random.shuffle(self.controller.players)

        self.current_turn["attacker"] = self.controller.players[0]

    def next_turn(self):
        self.current_turn["turn_count"] += 1

        self.current_turn["attacker"].select_target()

    def start_game(self):
        self.controller.table.distribute_chips()
        self.controller.table.deal_cards()

        self.shuffle_players()
        self.next_turn()
