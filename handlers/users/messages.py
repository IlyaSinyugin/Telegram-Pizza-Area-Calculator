from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
import numpy as np


# Only messages with digits in them will be passed here
@dp.message_handler(regexp='^[0-9]*$')
async def bot_area(message: types.Message):
    diameter = message.text
    area = np.pi * (int(diameter)/2) * (int(diameter)/2)
    await message.answer(f"The diameter you entered is {diameter}cm\n"
                         f"The area is {int(area)}cm^2")


# Handler that activates if the first one did not pass through
@dp.message_handler()
async def bot_wrongFormat(message: types.Message):
    await message.answer(f"Wrong format!"
                         f"Please, input digits")
