from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer

from widgets import BaseTerminal, GameLogoWidget


class Terminal(BaseTerminal):
    DEFAULT_CSS = """
    Terminal {

    }
    """


class MainMenuScreen(Screen):
    def compose(self) -> ComposeResult:
        with Terminal():
            yield Header(show_clock=True)
            yield Footer()

            yield GameLogoWidget()
