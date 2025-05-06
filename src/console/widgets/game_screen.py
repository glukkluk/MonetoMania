from textual.widgets import Label, Digits, ProgressBar, Rule
from textual.containers import Container, Vertical, Horizontal, Grid, Center


class CurrentGameState(Grid):
    class Countdown(Vertical):
        def compose(self):
            yield Center(Digits("56", id="timeout"))
            yield ProgressBar()

    def compose(self):
        yield Label("4:05")
        yield Container()

        yield self.Countdown()


class GameProcess(Vertical):
    class TableInfo(Grid):
        def compose(self):
            with Container(id="bet-container"):
                with Horizontal():
                    yield Label("15", id="attacker-bet")
                    yield Label("-:-")
                    yield Label("20", id="defender-bet")

            with Vertical(classes="commission-container"):
                yield Center(Label("3"))
                yield Rule()
                yield Center(Label("21"))

        def on_mount(self):
            self.id = "table-info"

    class TableCards(Grid):
        def compose(self):
            for _ in range(3):
                yield Center(Container(classes="empty"))

        def on_mount(self):
            self.id = "table-cards"

    def compose(self):
        yield self.TableInfo()

        yield self.TableCards()


class GameScreenWidget(Grid):
    def compose(self):
        yield CurrentGameState()
        yield GameProcess()
