from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer

from widgets import BaseTerminal


class Terminal(BaseTerminal):
    DEFAULT_CSS = """
    Terminal {
    }
    """


class CreateGameScreen(Screen):
    def compose(self) -> ComposeResult:
        with Terminal():
            yield Header(show_clock=True)
            yield Footer()
