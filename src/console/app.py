from textual.app import App


from screens import GameProcessScreen


class MonetoManiaApp(App):
    TITLE = "MonetoMania"
    CSS_PATH = "styles.tcss"

    def on_mount(self):
        self.install_screen(GameProcessScreen(), name="game-process-screen")

        self.push_screen("game-process-screen")
