from textual.widgets import Button


class CancelButton(Button):
    def on_mount(self):
        self.label = "Cancel"

    def on_button_pressed(self, event: Button.Pressed):
        self.app.pop_screen()


class CreateButton(Button):
    def on_mount(self):
        self.label = "Create"
