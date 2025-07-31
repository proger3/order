import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

# Загрузка токена
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Клавиатура меню
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("📁 База"))
menu_keyboard.add(KeyboardButton("✉️ Текст"))
menu_keyboard.add(KeyboardButton("📢 Рассылка"))

# Переменные для хранения данных
contacts = []
message_text = ""

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("👋 Бот готов к работе!", reply_markup=menu_keyboard)

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def handle_document(message: types.Document):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    await file.download(destination_file="contacts.xlsx")
    contacts.append("contacts.xlsx")  # Просто пример, нужно парсить файл
    await message.answer("✅ База загружена!")

@dp.message_handler(lambda msg: msg.text == "✉️ Текст")
async def set_text(message: types.Message):
    await message.answer("Введите текст рассылки:")
    
    @dp.message_handler()
    async def save_text(msg: types.Message):
        global message_text
        message_text = msg.text
        await msg.answer("✅ Текст сохранён!")

@dp.message_handler(lambda msg: msg.text == "📢 Рассылка")
async def start_mailing(message: types.Message):
    if not contacts or not message_text:
        await message.answer("❌ Нет базы или текста!")
        return
    
    await message.answer("Рассылка начата... (это тест, сообщения не отправляются)")
    # Здесь будет логика рассылки

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
