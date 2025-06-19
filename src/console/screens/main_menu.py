from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Button
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
        grid-rows: 2fr 1fr;
    }
    """


class MainMenuScreen(Screen):
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "create-game-button":
            self.app.push_screen("create-game-screen")

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
