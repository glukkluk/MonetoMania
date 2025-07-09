from textual.containers import Container, Grid
from textual.widgets import Label, Button


class NumberOfPlayersWidget(Container):
    def compose(self):
        yield Label("Choose the number of players", classes="widget-label")

        with Grid():
            yield Button("2")
            yield Button("3")
            yield Button("4")
            yield Button("5")
            yield Button("6")
