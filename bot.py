import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8994131331:AAFNUI1gjxBfNFBL0ppLLcd_j2V7pl9zeWc"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🔥 Fallen Angels Alliance Bot\n\n"
        "Бот работает!"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
