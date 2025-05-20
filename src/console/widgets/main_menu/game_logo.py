from textual.widgets import Label

LOGO_LABEL = """
 __  __                  _        __  __             _       
|  \/  |                | |      |  \/  |           (_)      
| \  / | ___  _ __   ___| |_ ___ | \  / | __ _ _ __  _  __ _ 
| |\/| |/ _ \| '_ \ / _ \ __/ _ \| |\/| |/ _` | '_ \| |/ _` |
| |  | | (_) | | | |  __/ || (_) | |  | | (_| | | | | | (_| |
|_|  |_|\___/|_| |_|\___|\__\___/|_|  |_|\__,_|_| |_|_|\__,_|
"""


class GameLogoWidget(Label):
    def on_mount(self, event):
        self.update(LOGO_LABEL)
