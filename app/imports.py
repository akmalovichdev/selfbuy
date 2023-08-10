from asyncore import dispatcher
from lib2to3.pytree import type_repr
from aiogram.dispatcher import Dispatcher
from app.settings.config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import app.settings.db as db
import app.other.keyboards as kb
import time
import schedule
import os.path
import openai
import app.settings.text as text
import asyncio
import pathlib
from pathlib import Path  
import logging
import tracemalloc
from aiogram.utils.exceptions import BotBlocked, ChatNotFound
import app.other.other as other