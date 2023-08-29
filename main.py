from aiogram import Bot, Dispatcher, types, executor
from config import token
import random

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадайте")

@dp.message_handler(text=["1", "2", "3"])
async def bot_random(message:types.Message):
    user = int(message.text)
    bot = random.randint(1, 3)
    if user == bot:
        await message.answer("Вы выиграли!")
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else:
        await message.answer("Вы проиграли!")
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

executor.start_polling(dp)