from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer

from widgets import (
    BaseTerminal,
    UserInventoryWidget,
    SidebarWidget,
    GameScreenWidget,
    InputWidget,
)


class Terminal(BaseTerminal):
    DEFAULT_CSS = """
    Terminal {
        grid-size: 2 3;
        grid-rows: 3fr 1fr 0.25fr;
        grid-columns: 1fr 3fr;
    }
    """


class GameProcessScreen(Screen):
    def compose(self) -> ComposeResult:
        with Terminal():
            yield Header(show_clock=True)
            yield Footer()

            # Sidebar with list of players
            yield SidebarWidget(num_players=5)

            #  Container with the game process
            yield GameScreenWidget()

            # Container with the user info (number of chips, and current cards)
            yield UserInventoryWidget(num_cards=6)

            # Input field
            yield InputWidget()
