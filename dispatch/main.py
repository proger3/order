from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

# Настройка бота
API_TOKEN = 'ВАШ_TELEGRAM_BOT_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Клавиатура меню
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("📁 База"))
menu_keyboard.add(KeyboardButton("✉️ Текст"))
menu_keyboard.add(KeyboardButton("📢 Рассылка"))

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("👋 Привет! Это бот для рассылки.", reply_markup=menu_keyboard)

# Обработчик кнопок
@dp.message_handler(lambda msg: msg.text in ["📁 База", "✉️ Текст", "📢 Рассылка"])
async def menu_buttons(message: types.Message):
    if message.text == "📁 База":
        await message.answer("Загрузите файл с базой контактов (Excel/CSV/TXT).")
    elif message.text == "✉️ Текст":
        await message.answer("Введите текст рассылки:")
    elif message.text == "📢 Рассылка":
        await message.answer("Выберите количество контактов:\n5K | 10K | 20K")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
