from textual.widgets import Input


class InputWidget(Input):
    def on_mount(self):
        self.placeholder = "Enter something..."
