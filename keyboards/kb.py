from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
'''#''''''''''''''''''''''''''''''''''''''''Запуск рулетки''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="Крутить", callback_data="Крутить")
kb = InlineKeyboardMarkup(row_width=1)
kb.insert(b1) #в ряд
'''#''''''''''''''''''''''''''''''''''''''''Запус крута''''''''''''''''''''''''''''''''''''''''''''#'''
b2  = InlineKeyboardButton(text="🎁", callback_data="Подарок")
kb1 = InlineKeyboardMarkup(row_width=1)
kb1.row(b2, b2, b2, b2, b2).row(b2, b2, b2, b2, b2).row(b2, b2, b2, b2, b2).row(b2, b2, b2, b2, b2).row(b2, b2, b2, b2, b2)
'''#''''''''''''''''''''''''''''''''''''''''Подробней о бонусах''''''''''''''''''''''''''''''''''''''''''''#'''
kb2 = InlineKeyboardMarkup()
button = InlineKeyboardButton('📖 Подробнее о бонусах', url='https://google.com')
kb2.add(button)