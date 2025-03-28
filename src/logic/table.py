import random
from typing import TYPE_CHECKING, LiteralString

if TYPE_CHECKING:
    from logic.controller import Controller


class Table:
    cards: list[LiteralString] = ("1 2 3 4 5 6 7 8 9 W S M".split(" ") * 8) + (
        "0 G U".split(" ") * 4
    )
    beaten_cards: list = []

    gain: int = 0

    current_commission: int = 0
    total_commission: int = 0

    def __init__(self, controller, bank: int):
        self.controller: Controller = controller
        self.bank: int = bank

        self.minimal_bet: int = int((self.bank / len(self.controller.players)) * 0.05)

    def distribute_chips(self):
        for player in self.controller.players:
            player.wallet = int(self.bank / len(self.controller.players))

        self.bank = 0

    def deal_cards(self):
        random.shuffle(self.cards)

        for player in self.controller.players:
            player.current_cards = self.cards[:6]
            self.cards = self.cards[6:]
