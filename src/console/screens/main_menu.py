from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer
from textual.containers import Center

from widgets import (
    BaseTerminal,
    GameLogoWidget,
    CreateGameButton,
    JoinTheGameButton,
    RulesButton,
    SettingsButton,
    AboutWidget,
)


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

            yield Center(GameLogoWidget())

            yield Center(CreateGameButton())
            yield Center(JoinTheGameButton())
            yield Center(RulesButton())
            yield Center(SettingsButton())

            yield Center(AboutWidget(text="About"))
