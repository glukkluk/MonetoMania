from textual.widgets import Button


class BaseButton(Button):
    DEFAULT_CSS = """
    BaseButton {
        
    }
    """


class CreateGameButton(BaseButton):
    def on_mount(self):
        self.label = "Create game"


class JoinToGameButton(BaseButton):
    def on_mount(self):
        self.label = "Join to game"


class RulesButton(BaseButton):
    def on_mount(self):
        self.label = "Rules"


class SettingsButton(BaseButton):
    def on_mount(self):
        self.label = "Settings"
