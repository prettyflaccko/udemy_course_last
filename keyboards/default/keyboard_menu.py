from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text='Tesla')
        ],
        [
            KeyboardButton(text='BMW')
        ],

        [
            KeyboardButton(text='Mercedes')
        ],
    ],
    resize_keyboard=True)

# keyboard = ReplyKeyboardMarkup(row_width=1)
# keyboard.add(InlineKeyboardButton(text='text'))