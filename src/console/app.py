from textual.app import App


from screens import (
    MainMenuScreen,
    CreateGameScreen,
    SetPlayersScreen,
    GameProcessScreen,
    StartGameScreen,
)


class MonetoManiaApp(App):
    TITLE = "MonetoMania"
    CSS_PATH = "styles.tcss"

    def on_mount(self):
        self.install_screen(MainMenuScreen(), name="main-menu-screen")
        self.install_screen(CreateGameScreen(), name="create-game-screen")
        self.install_screen(SetPlayersScreen(), name="set-players-screen")
        self.install_screen(GameProcessScreen(), name="game-process-screen")
        self.install_screen(StartGameScreen(), name="start-game-screen")

        self.push_screen("main-menu-screen")
