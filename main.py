from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start
import asyncio
import logging
from aiogram.filters import Command
from core.settings import settings
from core.untils.commands import set_commands
from core.handlers import recommendation
from core.untils.statesform import StepsForm


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id,  text = 'Бот остановлен!')
async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(recommendation.get_recommendatrion, Command(commands='get_recommendation'))
    dp.message.register(recommendation.expectation_rec, StepsForm.GET_FILM)

    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())