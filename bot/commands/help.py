from aiogram import types

from bot.commands.bot_commands import bot_commands


async def help_command(message: types.Message):

    return await message.answer(
        f"{bot_commands[0][0]} - {bot_commands[0][1]}\n\n{bot_commands[1][0]} - {bot_commands[1][1]}"
    )
