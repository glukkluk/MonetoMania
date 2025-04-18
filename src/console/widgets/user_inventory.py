from textual.containers import Container, Grid, Center
from textual.widgets import Digits


class UserInventoryWidget(Grid):
    def __init__(self, num_cards: int):
        super().__init__()

        self.num_cards: int = num_cards

    def compose(self):
        yield Center(Digits("100"), classes="user-chips")

        for _ in range(self.num_cards):
            yield Container(classes="empty")
