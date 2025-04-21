import os

from aiogram.types import Message, FSInputFile

from app.middleware import PermissionsMiddleware, InstagramVideoDownloadMiddleware
from app.service import InstagramReelsDownloadService
from app.handler import router

@router.message(PermissionsMiddleware(), InstagramVideoDownloadMiddleware())
async def handler(message: Message):
    filename = InstagramReelsDownloadService.download(message.text, filename)

    await message.bot.send_video(chat_id=message.chat.id, reply_to_message_id=message.message_id, video=FSInputFile(path=filename))

    os.remove(filename)