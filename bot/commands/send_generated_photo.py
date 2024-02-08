from aiogram import types, Bot
from aiogram.utils.chat_action import ChatActionSender
from translate import Translator

from bot.generation.create_image import generate


UK_LETTERS = "абвгґдеєжзиіїйклмнопрстуфзцчшщьюя"


async def translating(text: str) -> str:
    if text[0].lower() in UK_LETTERS:
        translator = Translator(from_lang="uk", to_lang="en")
        translated_text = translator.translate(text)
        return translated_text
    else:
        return text


async def upload_photo(message: types.Message, bot: Bot):
    async with ChatActionSender.upload_photo(chat_id=message.chat.id, bot=bot):
        image_url = generate(prompt=await translating(message.text))
        photo = types.URLInputFile(url=image_url)

        await bot.send_photo(chat_id=message.chat.id, photo=photo)
