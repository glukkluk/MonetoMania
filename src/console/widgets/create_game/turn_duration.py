from textual.containers import Container, Grid
from textual.widgets import Label, Button


class TurnDurationWidget(Container):
    def compose(self):
        yield Label(
            "Select the duration of the player's turn",
            classes="turn-duration-label",
        )

        with Grid():
            yield Button("10")
            yield Button("20")
            yield Button("30")
            yield Button("45")
            yield Button("60")
