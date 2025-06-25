from .terminal import BaseTerminal

from .main_menu.game_logo import GameLogoWidget
from .main_menu.buttons import (
    CreateGameButton,
    JoinTheGameButton,
    RulesButton,
    SettingsButton,
)
from .main_menu.about import AboutWidget

from .create_game.game_name import GameNameWidget
from .create_game.entrance_fee import EntranceFeeWidget
from .create_game.turn_duration import TurnDurationWidget

from .game_process.user_inventory import UserInventoryWidget
from .game_process.sidebar import SidebarWidget
from .game_process.game_screen import GameScreenWidget
from .game_process.input import InputWidget

__all__: list[str] = [
    "BaseTerminal",

    "GameLogoWidget",
    "CreateGameButton",
    "JoinTheGameButton",
    "RulesButton",
    "SettingsButton",
    "AboutWidget",

    "GameNameWidget",
    "EntranceFeeWidget",
    "TurnDurationWidget",

    "UserInventoryWidget",
    "SidebarWidget",
    "GameScreenWidget",
    "InputWidget",
]
