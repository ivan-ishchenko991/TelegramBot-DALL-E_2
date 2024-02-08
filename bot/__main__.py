import os
import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from commands import register_user_commands
from commands.bot_commands import bot_commands


async def main():
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(token=os.getenv('TOKEN'))
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("---"*20, "\nBot stopped\n", "---"*20)
