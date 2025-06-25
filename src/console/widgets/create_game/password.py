from textual.containers import Grid
from textual.widgets import Label, Input, Checkbox


class PasswordWidget(Grid):
    def compose(self):
        self.password_input = Input(disabled=True)

        yield Label("Password", classes="password-label")

        yield Checkbox()
        yield self.password_input

    def on_checkbox_changed(self, event: Checkbox.Changed):
        value = event.value

        self.password_input.disabled = not value

        if not value:
            self.password_input.clear()
