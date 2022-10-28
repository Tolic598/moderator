from multiprocessing import context
from shutil import ignore_patterns
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from numpy import equal
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text

# class FSMadmin(StatesGroup):
#     photo=State()
#     name=State()
#     descriptions=State()
#     price=State()
    

# # @dp.message_handler(commands='Загрузить', state=None)
# async def cm_start(message: types.Message):
#     await FSMadmin.photo.set()
#     await message.reply("Загрузи фото:")
#     # await FSMadmin.password.set()

# # @dp.message_handler(content_types=['photo'], state=FSMadmin.photo)
# async def load_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#     await state.finish()
#     await message.reply("ок")

# async def load_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await FSMadmin.next()
#     await message.reply("Тепень введи описание:")

# async def load_descriptions(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['descriptions'] = message.text
#     await FSMadmin.next()
#     await message.reply("Тепень введи цену:")

# async def load_price(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['price'] = float(message.text)
#     async with state.proxy() as data:
#         await message.reply(str(data))
#     await state.finish()

# async def cancel_handler(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply("ок")

# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(cm_start, Text(equals="Добавить логин", ignore_case=None))
#     dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    
    # dp.register_message_handler(load_name, state=FSMadmin.name)
    # dp.register_message_handler(load_descriptions, state=FSMadmin.descriptions)
    # dp.register_message_handler(load_price, state=FSMadmin.price)
    # dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")