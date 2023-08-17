from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from pip import main
import app.settings.db as db

###############################################################################################################################################################

def admin_menu():
	button1 = KeyboardButton('Статистика')
	button2 = KeyboardButton('Рассылка')
	button3 = KeyboardButton('Назад')
	admin1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	admin1_kb.add(button1)
	admin1_kb.add(button2)
	admin1_kb.add(button3)
	return admin1_kb
	
def back():
	back_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	button = KeyboardButton('Отмена')
	back_kb1.add(button)
	return back_kb1

###############################################################################################################################################################

def menu(message):
    main = InlineKeyboardMarkup()
    questions = InlineKeyboardButton(text='Ответить на вопросы', callback_data='questions')
    main.add(questions)
    return main

def newQuestion(message):
    main = InlineKeyboardMarkup()
    questions = InlineKeyboardButton(text='Разместить новый выкуп', callback_data='questions')
    main.add(questions)
    return main

def questions(call, type):
    main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if type == 'purchasePurpose':
        main.add(KeyboardButton('Отзывы'))
        main.add(KeyboardButton('Продвижение'))
        main.add(KeyboardButton('Забор товара'))
    elif type == 'isProductRetrievalPlanned':
        main.add(KeyboardButton('Да, заберу сам'))
        main.add(KeyboardButton('Да, заберет курьер'))
        main.add(KeyboardButton('Покупатель может оставить товар себе'))
        main.add(KeyboardButton('Товар надо будет вернуть на ПВЗ'))
    elif type == 'isBuyerRetrievalNeeded':
        main.add(KeyboardButton('Да, покупателю надо забрать с ПВЗ'))
        main.add(KeyboardButton('Нет, заберу товар сам'))
    elif type == 'isReviewNeeded':
        main.add(KeyboardButton('Да'))
        main.add(KeyboardButton('Да, желательно с фото'))
        main.add(KeyboardButton('Нет'))
    main.add(KeyboardButton('Отмена'))
    return main

def privacy(message):
    main = InlineKeyboardMarkup()
    yes = InlineKeyboardButton(text='Ознакомился. Отправить на модерацию.', callback_data='yes')
    back = InlineKeyboardButton(text='Отмена', callback_data='back')
    main.add(yes)
    main.add(back)
    return main

def publish(message, id):
    main = InlineKeyboardMarkup()
    publish = InlineKeyboardButton(text='Опубликовать', callback_data=f'publish-{id}')
    link_button = InlineKeyboardButton("Написать", url=f"tg://user?id={message.from_user.id}")
    main.add(link_button)
    main.add(publish)
    return main