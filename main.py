from aiogram.utils import executor
from app.settings.config import dp, bot

from app.handlers import admin, start, questions, publish

import schedule
import app.settings.db as db
import asyncio

admin, start, questions, publish

@dp.errors_handler()
async def errors_handler(update, exception):
    chat_id = db.selectConf('errorGroup')
    await bot.send_message(chat_id, text=f'Произошла ошибка: {exception}') # отправляем уведомление в телеграм

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except:
        None