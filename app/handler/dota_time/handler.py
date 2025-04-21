from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.config import Config
from app.middleware import PermissionsMiddleware, DotatimeMiddleware
from app.handler import router

@router.message(
    PermissionsMiddleware(),
    DotatimeMiddleware(),
    Command('dotatime'),
)
async def handler(message: Message):
    await message.bot.send_message(
        chat_id=message.chat.id,
        text=f'Дота? {" ".join(map(lambda x: "@" + x, Config.get_dota_players()))}',
    )