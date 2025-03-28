from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logic.controller import Controller


class Player:
    wallet: int = 0
    current_cards: list = []

    def __init__(self, controller, name: str):
        self.controller: Controller = controller
        self.name: str = name

    # def print_myself(self):
    #     self.controller.console.print(
    #         f"[bold green]Name: {self.name}\n[/]"
    #         f"[red]Wallet: {self.wallet}\n[/]"
    #         f"[yellow]Cards: {" ".join(self.current_cards)}\n[/]"
    #     )

    def select_target(self):
        # self.print_myself()

        is_correct_input = False

        while not is_correct_input:
            target = input("Enter the name of the target: ")

            for player in self.controller.players:
                if target == player.name:
                    self.controller.game.current_turn["target"] = player

                    if (
                        self.controller.game.current_turn["target"]
                        == self.controller.game.current_turn["attacker"]
                    ):
                        print("You can't attack yourself!")
                        break

                    is_correct_input = True
                    break

            else:
                print("Player not found! Try again.")
                continue

        else:
            print(f"You selected {target} as your target.")

    def place_a_bet(self):
        is_correct_input = False

        while not is_correct_input:
            bet = int(input("Enter your bet: "))

            if bet > self.wallet:
                print("You don't have enough money to bet that much!")

            elif bet < self.controller.table.minimal_bet:
                print(
                    f"You need to bet at least {self.controller.table.minimal_bet} chips!"
                )

            else:
                is_correct_input = True

    def place_cards(self):
        pass

    def beat_the_cards(self):
        pass
