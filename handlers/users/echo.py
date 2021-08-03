from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
import numpy as np


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    diameter = message.text
    area = np.pi * (int(diameter)/2) * (int(diameter)/2)
    await message.answer(f"The diameter you entered is {diameter}cm\n"
                         f"The area is {int(area)}cm^2")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
