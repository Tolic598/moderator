from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5751189257:AAFsJM6naWKoRx6pNGAHLvEiOEgGb8hN9Zs'
storage=MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
