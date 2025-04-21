import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import app.handler as handlers
import app.config

dp = Dispatcher()

dp.include_routers(handlers.router)

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=app.config.Config.get_bot_token(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # await bot.set_my_commands(scope=BotCommandScopeAllPrivateChats(), commands=[
    #     BotCommand(command='/dotatime', description='Позвать пацанов в доту'),
    # ])

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
