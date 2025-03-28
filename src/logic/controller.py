from logic.game import Game
from logic.table import Table
from logic.players import Player

from typing import List

from dataclasses import dataclass, field


@dataclass
class Controller:
    game: Game = None
    table: Table = None
    players: List[Player] = field(default_factory=list)

    def create_game(self, **kwargs) -> Game:
        self.game = Game(controller=self, **kwargs)

        return self.game

    def create_table(self, bank, **kwargs) -> Table:
        self.table = Table(controller=self, bank=bank, **kwargs)

        return self.table

    def create_player(self, name, **kwargs) -> Player:
        player = Player(controller=self, name=name, **kwargs)
        self.players.append(player)

        return player
