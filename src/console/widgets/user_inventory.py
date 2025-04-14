from textual.containers import Container, Horizontal, Center
from textual.widgets import Digits, Label


class UserInventoryWidget(Horizontal):
    def compose(self):
        yield Center(Digits("100"), classes="user-chips")

        for i in range(6):
            yield Container(Label(f"Card: {i}", classes=f"user-card{i + 1}"))
