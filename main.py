from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

API_TOKEN = "6576441032:AAFXa5j-z-zR6-lOuD1wj3gSqBK2SG2z4Pg"

# Создаем бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Получаем имя пользователя
    user_name = message.from_user.first_name
    # Создаем клавиатуру с кнопкой "Перейти к темам"
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton("Получить методичку", url='https://solarmary.github.io/profimatika17.github.io/'))
    await message.answer(f"Привет, {user_name}! Добро пожаловать в наш бот! Нажмите кнопку ниже, чтобы перейти к методичке по со всеми необходимыми фактами по планиметрии.", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
