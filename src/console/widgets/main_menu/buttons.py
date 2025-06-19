from textual.widgets import Button


class BaseButton(Button):
    DEFAULT_CSS = """
    BaseButton {
        
    }
    """


class CreateGameButton(BaseButton):
    def on_mount(self):
        self.label = "Create game"
        self.id = "create-game-button"


class JoinTheGameButton(BaseButton):
    def on_mount(self):
        self.label = "Join the game"


class RulesButton(BaseButton):
    def on_mount(self):
        self.label = "Rules"


class SettingsButton(BaseButton):
    def on_mount(self):
        self.label = "Settings"
