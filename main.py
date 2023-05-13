from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv   # for .env
import os


load_dotenv()

bot = Bot(os.getenv('TOKEN_API'))
dp = Dispatcher(bot)

# это команда чтобы запустит бота
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name},Welcome our device shop')


# если юзер не понятный команду
@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer("I don't understand you")

if __name__ == '__main__':
    executor.start_polling(dp)