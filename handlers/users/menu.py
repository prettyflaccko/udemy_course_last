from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Выберите автомобиль из меню ниже', reply_markup=menu)


@dp.message_handler(text='Tesla')
async def get_bmw(message: types.Message):
    await message.answer('Вы выбрали Tesla')


@dp.message_handler(Text(equals=['Tesla', 'BMW', 'Mercedes']))
async def get_cars(message: types.Message):
    await message.answer(f'Вы выбрали: {message.text}', reply_markup=ReplyKeyboardRemove())
