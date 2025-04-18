from textual.containers import ScrollableContainer
from textual.widgets import RadioButton, RadioSet


class SidebarWidget(ScrollableContainer):
    def __init__(self, num_players: int):
        super().__init__()

        self.num_players: int = num_players

    def compose(self):
        with RadioSet():
            for _ in range(self.num_players):
                yield RadioButton("Player")
