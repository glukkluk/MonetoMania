from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logic.controller import Controller


class Player:
    wallet: int = 0
    current_cards: list = []

    def __init__(self, controller, name: str):
        self.controller: Controller = controller
        self.name: str = name

    def select_target(self, target: str):
        for player in self.controller.players:
            if target == player.name:
                self.controller.game.current_turn["target"] = player

                if (
                    self.controller.game.current_turn["target"]
                    == self.controller.game.current_turn["attacker"]
                ):
                    return "You can't attack yourself!"

                return f"You selected {target} as your target."

        else:
            return "Player not found! Try again."

    def place_a_bet(self, bet: int):
        if bet > self.wallet:
            return "You don't have enough chips to bet that much!"

        elif bet < self.controller.table.minimal_bet:
            return (
                f"You need to bet at least {self.controller.table.minimal_bet} chips!"
            )

        else:
            self.wallet -= bet
            self.controller.table.gain += bet

            return f"You bet {int(bet)} chips."
