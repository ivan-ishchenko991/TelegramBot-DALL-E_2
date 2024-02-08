from aiogram import types

from bot.keyboards import start_menu


async def start(message: types.Message):
    await message.answer(
        "Привіт!\nЯ бот для генерації зображень. Просто напиши мені, яке саме зображення тобі потрібно.\n\nHello!"
        "\nI am an image generation bot. Just write to me and tell me what kind of image you need.",
        reply_markup=start_menu
    )
