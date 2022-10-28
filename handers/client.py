from matplotlib.pyplot import text
from keyboards import kb, kb1, kb2
from multiprocessing import context
from shutil import ignore_patterns
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
import random
from aiogram import types
import time

class FSMadmin(StatesGroup):
    photo=State()
    login=State()
    password=State()
    reg_login=State()
    reg_password=State()

# member = await bot.get_chat_member(message.chat.id, message.from_user.id)
# print(member.is_chat_admin())  проверка на админа

text=['мат']

async def antimat(message: types.Message):
    if any(word in message.text.lower() for word in text):
        await message.answer(f'@{message.from_user.username} ты сказал?')
        await message.delete()


'''#''''''''''''''''''''''''''''''''''''''''Запуск бота''''''''''''''''''''''''''''''''''''''''''''#'''
async def start_bot(message: types.Message):
    await message.reply("👨‍🔧  приветствует Вас!\nЯ могу предложить следующие функции:\n1)/install — инструкция установки;\n2)/teams — список всех команд с их описанием;\n3)/help  — помощь;\n4)/bonus — какие есть бонусы во вселенной ;\n")
    await bot.get_chat_member(message.chat.id, message.from_user.id)


'''#''''''''''''''''''''''''''''''''''''''''функции бота''''''''''''''''''''''''''''''''''''''''''''#'''
async def installation_bot(message: types.Message):
    await message.reply("✅ Установка довольно проста:\n\n1) Пригласите бота по этой ссылке;\n2) Нажмите на название СВОЕГО чата, после на карандаш сверху;\n3) Перейдите в пункт «Администраторы»;\n4) Нажмите на кнопку «Добавить администратора»;\n5) Выберите из списка  и нажмите на галочку.\n\n💬 Воспользуйтесь фотографией или видео-гайдом, они вам помогут.\nПосле выдачи админки, пропишите «/admin» для проверки работоспособности.")

async def teams_bot(message: types.Message):
    await message.reply("👨‍🔧")

async def help_bot(message: types.Message):
    await message.reply("👨‍🔧")

async def bonuses_bot(message: types.Message):
    await message.reply("🎁 Бонусы — это небольшое расширение возможностей бота в вашем чате.\n🍬 Бонусы приобретаются на виртуальную валюту вселенной.\n1) <b>💎 VIP-статус</b>\n2) 🔴 Банхаммер\n3) 💫 Плюсопад\n4) 👎 Минусит\n5) 🤫 Анонимка\n6) ❓ Анонимка рп\n", reply_markup=kb2, parse_mode = types.ParseMode.HTML)
'''#''''''''''''''''''''''''''''''''''''''''все команды бота''''''''''''''''''''''''''''''''''''''''''''#'''
async def fortune(message: types.Message):
     await message.reply("Вас приветствует Купидон счастья от", reply_markup=kb)

'''#''''''''''''''''''''''''''''''''''''''''приветствия нового пользователя в чате''''''''''''''''''''''''''''''''''''''''''''#'''
async def greetings(message: types.Message):
    name=message.from_user.first_name
    famili=message.from_user.last_name
    msg = await message.answer(f"Добро пожаловать {name}, в наш чат\n\nПравила:\n1.Без посторонних линков❌\n2.Политика - БАН🥶\n3.Реклама - БАН🤐\n4.Слил наш код?-БАН НАВСЕГДА🐀 🐀\nА так общайтесь на здоровье 😄\nДелитесь кодами и забирайте от админа призы)😊")
    time.sleep(10)
    await msg.delete()
    time.sleep(10)


'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн''''''''''''''''''''''''''''''''''''''''''''#'''
async def fortune_btn(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выбери один из подарков", reply_markup=kb1)

async def prize_btn(call: CallbackQuery):
    await call.message.delete()
    balance = 0
    balance_ran = random.randint(50,1000)
    balance += balance_ran
    await call.message.answer(f"Приз: {balance_ran}\nБаланс: {balance}", reply_markup=kb1)

'''#''''''''''''''''''''''''''''''''''''''''регистр''''''''''''''''''''''''''''''''''''''''''''#'''
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'])
    dp.register_message_handler(antimat)
    dp.register_message_handler(installation_bot, commands=['install'])
    dp.register_message_handler(teams_bot, commands=['teams'])
    dp.register_message_handler(help_bot, commands=['help'])
    dp.register_message_handler(bonuses_bot, commands=['bonus'])
    dp.register_message_handler(greetings, content_types=['new_chat_members'])
    dp.register_message_handler(fortune, commands=['fortuna'])
    dp.register_callback_query_handler(fortune_btn, text="Крутить")
    dp.register_callback_query_handler(prize_btn, text="Подарок")
    # dp.register_message_handler(cm_photo, Text(equals="Добавить фото", ignore_case=None))
    # dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)


