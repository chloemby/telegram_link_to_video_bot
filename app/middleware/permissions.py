from aiogram.filters import BaseFilter

from app.config import Config
from aiogram.types import Message


class PermissionsMiddleware(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.username in Config.get_allow_list()