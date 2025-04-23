from textual.widgets import Label, Digits, ProgressBar
from textual.containers import Container, Vertical, Grid, Center


class CurrentGameState(Grid):
    def compose(self):
        yield Label("4:05")
        yield Container()
        with Vertical():
            yield Center(Digits("56", id="timeout"))
            yield ProgressBar()


class GameProcess(Container):
    pass


class GameScreenWidget(Grid):
    def compose(self):
        yield CurrentGameState()
        yield GameProcess()
