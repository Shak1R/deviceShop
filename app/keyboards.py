from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Category').add('Basket').add('Contact')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Category').add('Basket').add('Contact').add('Admin Panel')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Add new Device').add('Delete device').add('Make a newsletter')

category_list = InlineKeyboardMarkup(row_width=2)
category_list.add(InlineKeyboardButton(text='Phones', callback_data='phones'),
                  InlineKeyboardButton(text='Laptops', callback_data='laptops'),
                  InlineKeyboardButton(text='Headphones', callback_data='headphones'))