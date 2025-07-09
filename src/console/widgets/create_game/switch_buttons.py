from textual.widgets import Button


class BackButton(Button):
    def __init__(self, label=None):
        super().__init__(label=label)

    def on_button_pressed(self, event: Button.Pressed):
        self.app.pop_screen()


class NextButton(Button):
    def __init__(self, next_screen: str, label=None):
        super().__init__(label=label)
        self.next_screen = next_screen

    def on_button_pressed(self, event: Button.Pressed):
        self.app.push_screen(self.next_screen)
