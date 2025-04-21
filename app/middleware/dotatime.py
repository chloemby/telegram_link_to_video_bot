from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.config import Config


class DotatimeMiddleware(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.id == Config.get_dotatime_chat_id()