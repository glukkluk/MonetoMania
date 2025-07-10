from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Container, Center
from textual.widgets import Header, Footer

from widgets import (
    BaseTerminal,
    GameNameWidget,
    SearchUserNameWidget,
    EntranceFeeWidget,
    TurnDurationWidget,
    PasswordWidget,
    NumberOfPlayersWidget,
    BackButton,
    NextButton,
)


class StyleContainer(Container):
    DEFAULT_CSS = """
    StyleContainer {
        margin: 6 16;
    }
    """


class CreateGameScreen(Screen):
    def compose(self) -> ComposeResult:
        with BaseTerminal():
            yield Header(show_clock=True)
            yield Footer()

            with StyleContainer():
                yield GameNameWidget()
                yield EntranceFeeWidget()
                yield TurnDurationWidget()
                yield PasswordWidget()
                yield Center(BackButton(label="Cancel"))
                yield Center(NextButton(label="Next", next_screen="set-players-screen"))


class SetPlayersScreen(Screen):
    def compose(self):
        with BaseTerminal():
            yield Header(show_clock=True)
            yield Footer()

            with StyleContainer():
                yield SearchUserNameWidget()
                yield NumberOfPlayersWidget()

                yield Center(BackButton(label="Back"))
                yield Center(
                    NextButton(label="Create", next_screen="game-process-screen")
                )
