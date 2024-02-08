__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.commands.help import help_command
from bot.commands.start import start
from bot.commands.send_generated_photo import upload_photo


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(help_command, F.text == "Довідка")
    router.message.register(upload_photo, F.text)

