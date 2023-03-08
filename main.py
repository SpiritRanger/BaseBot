import logging
import re
from aiogram.bot.bot import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram import types
from aiogram import executor

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5963818558:AAGJWEFgVX5x_hGnJR-JZ6kFhItDeXp0C_A")
dp = Dispatcher(bot)


# Base answer
@dp.message_handler(content_types=['text'])
async def base_answer(message: types.Message):
    if contains_base_word(message.text):
        nato_flag = types.InputFile("nato-flag.gif")
        await message.reply_animation(animation=nato_flag)
    if contains_department_of_defense(message.text):
        nato_flag = types.InputFile("Pentagon.gif")
        await message.reply_animation(animation=nato_flag)


def contains_base_word(message_text: str):
    words = re.split(';|,|\.|[ ]|\"|\'|\?|!|\n|\r|-|@|#|&|%|~|\$|\+', message_text.lower())
    # logging.log(logging.INFO, words)
    return words.__contains__("база") or words.__contains__("base")

def contains_department_of_defense(message_text: str):
    words = re.split(';|,|\.|[ ]|\"|\'|\?|!|\n|\r|-|@|#|&|%|~|\$|\+', message_text.lower())
    # logging.log(logging.INFO, words)
    return words.__contains__("генштаб") or (words.__contains__("department") and words.__contains__("defense")) or (words.__contains__("генеральный") and words.__contains__("штаб"))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
