import sys
import os

# Add the parent directory of the current file to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from logic.controller import Controller

if __name__ == "__main__":
    try:
        controller = Controller()

        controller.create_player("Bob")
        controller.create_player("Alice")
        controller.create_player("John")
        controller.create_player("Mary")
        controller.create_player("Tom")

        controller.create_table(bank=1200)

        game = controller.create_game()
        game.start_game()

    except KeyboardInterrupt:
        console = Console()

        console.print(
            Panel(Text("Game stopped...", style="bold red"), expand=False),
            new_line_start=True,
        )
