from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import app.settings.db as db
import configs

token = db.selectConf('botToken')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
