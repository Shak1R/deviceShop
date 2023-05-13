from aiogram import Bot, Dispatcher, executor, types
from app import keyboards as kb
from app import database as db
from dotenv import load_dotenv   # for .env
import os


load_dotenv()

bot = Bot(os.getenv('TOKEN_API'))
dp = Dispatcher(bot)


async def on_start(_):
    await db.db_start()
    print("Successfully started")

# это команда чтобы запустит бота
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAICKWRfavfUNI-R9Bz-mTmRaYQkeqQFAAI3BwACYyviCaOcLOs6Zy0NLwQ')
    await message.answer(f'{message.from_user.first_name},Welcome our device shop',
                         reply_markup=kb.main)  # we add keyboards to bot
    await message.delete()
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'You are logged in as an administrator',
                             reply_markup=kb.main_admin)


@dp.message_handler(text='Category')
async def command_category(message: types.Message):
    await message.answer(f'Owner contact: @Shakir_Kadirov',
                         reply_markup=kb.category_list)


@dp.message_handler(text='Basket')
async def command_basket(message: types.Message):
    await message.answer(f'Owner contact: @Shakir_Kadirov')


@dp.message_handler(text='Contact')
async def command_contact(message: types.Message):
    await message.answer(f'Owner contact: @Shakir_Kadirov')


@dp.message_handler(text='Admin Panel')
async def command_contact(message: types.Message):
    await message.answer(f'You are logged into the admin panel',
                         reply_markup=kb.admin_panel)

@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 'phones':
        await bot.send_message(chat_id=callback_query.from_user, text='You are choose phones')
    elif callback_query.data == 'laptops':
        await bot.send_message(chat_id=callback_query.from_user, text='You are choose laptops')
    elif callback_query.data == 'headphones':
        await bot.send_message(chat_id=callback_query.from_user, text='You are choose headphones')


# если юзер не понятный команду
@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer("I don't understand you")


if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_start, skip_updates=True)