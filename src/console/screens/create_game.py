from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer

from widgets import (
    BaseTerminal,
    GameNameWidget,
    EntranceFeeWidget,
    TurnDurationWidget,
    PasswordWidget,
)


class Terminal(BaseTerminal):
    DEFAULT_CSS = """
    Terminal {
    }
    """


class StyleContainer(Container):
    DEFAULT_CSS = """
    StyleContainer {
        margin: 6 16;
    }
    """


class CreateGameScreen(Screen):
    def compose(self) -> ComposeResult:
        with Terminal():
            yield Header(show_clock=True)
            yield Footer()

            with StyleContainer():
                yield GameNameWidget()
                yield EntranceFeeWidget()
                yield TurnDurationWidget()
                yield PasswordWidget()
