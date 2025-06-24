from textual.widgets import Input


class GameNameWidget(Input):
    def on_mount(self):
        self.placeholder = "Game name:"
