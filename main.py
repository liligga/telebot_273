from aiogram import Bot, Dispatcher, executor, types
import logging
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def hello(message: types.Message):
    # await message.answer("Привет")
    await message.reply("Привет")
    # with open('images/cat.jfif', 'rb') as img:
    #     await message.answer_photo(photo=img)
        
# @dp.message_handler(commands=["info"])
# async def info(message: types.Message):
    # message.from_user
    # pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)
