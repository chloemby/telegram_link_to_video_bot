import asyncio
import logging
import os
import random
import sys
from urllib.parse import urlparse

from yt_dlp import YoutubeDL
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, FSInputFile

TOKEN = os.getenv('BOT_TOKEN')
dp = Dispatcher()


@dp.message()
async def handle_chat_message(message: Message):
    url = urlparse(message.text)
    if url.scheme == '':
        # not url message
        return

    if url.netloc.endswith('instagram.com') and url.path.startswith('/reel/'):
        filename = f'content/{random.randint(0, 1000000000)}.mp4'
        download_instagram_reel(message.text, filename)

        await message.bot.send_video(chat_id=message.chat.id, reply_to_message_id=message.message_id, video=FSInputFile(path=filename))

        os.remove(filename)


def download_instagram_reel(url, filepath):
    # Configure yt-dlp to download the best available quality
    ydl_opts = {
        'format': 'mp4',  # Highest video and audio quality
        'outtmpl': filepath, # Save to Colab's content directory
        'merge_output_format': 'mp4',  # Output format
        'quiet': False,  # Show download progress
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"❌ Error: {e}")



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
