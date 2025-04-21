from typing import List

import yaml

class Config:
    __CONFIG_PATH = 'config.yaml'

    __allow_list: List[str]
    __bot_token: str
    __dotatime_chat_id: int
    __dota_players: List[str]

    def __init__(self):
        config = yaml.safe_load(open(self.__CONFIG_PATH))['config']

        self.__allow_list = config['allowed_users']
        self.__bot_token = config['bot_token']
        self.__dotatime_chat_id = int(config['dotatime_chat'])
        self.__dota_players = config['dota_players']

    def get_allow_list(self) -> List[str]:
        return self.__allow_list

    def get_bot_token(self) -> str:
        return self.__bot_token

    def get_dotatime_chat_id(self) -> int:
        return self.__dotatime_chat_id

    def get_dota_players(self) -> List[str]:
        return self.__dota_players


config = Config()