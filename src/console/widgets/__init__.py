from .terminal import BaseTerminal

from .main_menu.game_logo import GameLogoWidget
from .main_menu.buttons import (
    CreateGameButton,
    JoinTheGameButton,
    RulesButton,
    SettingsButton,
)
from .main_menu.about import AboutWidget

from .create_game.names import GameNameWidget, SearchUserNameWidget
from .create_game.entrance_fee import EntranceFeeWidget
from .create_game.turn_duration import TurnDurationWidget
from .create_game.password import PasswordWidget
from .create_game.number_of_players import NumberOfPlayersWidget
from .create_game.general_info import GeneralInfoWidget
from .create_game.switch_buttons import BackButton, NextButton

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
    "SearchUserNameWidget",
    "EntranceFeeWidget",
    "TurnDurationWidget",
    "PasswordWidget",
    "NumberOfPlayersWidget",
    "GeneralInfoWidget",
    "BackButton",
    "NextButton",

    "UserInventoryWidget",
    "SidebarWidget",
    "GameScreenWidget",
    "InputWidget",
]
