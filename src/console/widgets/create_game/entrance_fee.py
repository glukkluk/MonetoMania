from textual.containers import Grid
from textual.widgets import Button, Input, Label


class EntranceFeeWidget(Grid):
    def compose(self):
        self.entrance_fee_input = Input(type="integer", value="100")

        yield Label("Entrance fee", classes="entrance-fee-label")

        yield Button("-", id="minus")
        yield self.entrance_fee_input
        yield Button("+", id="plus")

    def on_button_pressed(self, event: Button.Pressed):
        try:
            value = int(self.entrance_fee_input.value)

            match event.button.id:
                case "minus":
                    if value != 100:
                        self.entrance_fee_input.value = str(value - 100)

                    else:
                        self.notify("The minimum entry fee is 100")

                case "plus":
                    self.entrance_fee_input.value = str(value + 100)

        except ValueError:
            self.entrance_fee_input.value = "100"

    def on_input_changed(self, event: Input.Changed):
        # The final entrance fee of the user who wrote in the input field or clicked on the “+”/“-” buttons
        self.user_entrance_fee = event.value
