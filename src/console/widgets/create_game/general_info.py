from textual.containers import Container
from textual.widgets import Label, Collapsible


class GeneralInfoWidget(Container):
    def compose(self):
        yield Label("Game name: ")
        yield Label("Entrance fee: ")
        yield Label("Duration of the player's turn: ")
        yield Label("Password: ")
        yield Label("Number of players: ")

        with Collapsible(title="List of players:"):
            yield Label("*Each player's name*")
