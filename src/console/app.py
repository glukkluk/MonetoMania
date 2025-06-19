from textual.app import App


from screens import MainMenuScreen, CreateGameScreen, GameProcessScreen


class MonetoManiaApp(App):
    TITLE = "MonetoMania"
    CSS_PATH = "styles.tcss"

    def on_mount(self):
        self.install_screen(MainMenuScreen(), name="main-menu-screen")
        self.install_screen(CreateGameScreen(), name="create-game-screen")
        self.install_screen(GameProcessScreen(), name="game-process-screen")

        self.push_screen("main-menu-screen")
