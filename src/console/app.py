from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer


from widgets import UserInventoryWidget, SidebarWidget, GameScreenWidget


class Terminal(Grid):
    DEFAULT_CSS = """
    Terminal {
        height: 40;
        width: 90;

        grid-size: 2 2;
        grid-rows: 3fr 1fr;
        grid-columns: 1fr 3fr;
    }
    """


class MonetoManiaApp(App):
    TITLE = "MonetoMania"
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        with Terminal():
            yield Header(show_clock=True)
            yield Footer()

            # Sidebar with list of players
            yield SidebarWidget()

            #  Container with the game process
            yield GameScreenWidget()

            # Container with the user info (number of chips, and current cards)
            yield UserInventoryWidget()
