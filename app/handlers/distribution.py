from app.imports import *
import tracemalloc

tracemalloc.start()

class diskState(StatesGroup):
    productLink = State()
    cashback = State()
    algoritm = State()
    cashbackDay = State()
    isRulesAgreed = State()
    success = State()

@dp.callback_query_handler(text=['distribution'])
async def distribution(call: types.CallbackQuery, state: FSMContext):
    await other.deleteMessage(call.message.chat.id, call.message.message_id)
    await bot.send_message(call.message.chat.id, f'{text.distribution(call, "productLink")}', reply_markup = kb.back())
    await diskState.productLink.set()

@dp.message_handler(state=diskState.productLink, content_types=types.ContentType.TEXT)
async def productLink(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(productLink = message.text)
        await message.reply(f'{text.distribution(message, "cashback")}', reply_markup = kb.distribution(message, 'cashback'))
        await diskState.cashback.set()

@dp.message_handler(state=diskState.cashback, content_types=types.ContentType.TEXT)
async def cashback(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(cashback = message.text)
        await message.reply(f'{text.distribution(message, "algoritm")}', reply_markup = kb.back())
        await diskState.algoritm.set()

@dp.message_handler(state=diskState.algoritm, content_types=types.ContentType.TEXT)
async def algoritm(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(algoritm = message.text)
        await message.reply(f'{text.distribution(message, "cashbackDay")}', reply_markup = kb.distribution(message, "cashbackDay"))
        await diskState.cashbackDay.set()

@dp.message_handler(state=diskState.cashbackDay, content_types=types.ContentType.TEXT)
async def cashbackDay(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(cashbackDay = message.text)
        await message.reply(f'{text.distribution(message, "isRulesAgreed")}', reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(message.chat.id, f'{text.distribution(message, "privacy")}', reply_markup=kb.privacy(message))
        await diskState.isRulesAgreed.set()

@dp.callback_query_handler(state=diskState.isRulesAgreed)
async def isRulesAgreed(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'yes':
        await other.deleteMessage(call.message.chat.id, call.message.message_id)
        data = await state.get_data()
        id = db.addPurchase(call, data, 'distribution')
        await bot.send_message(call.from_user.id, f'{text.distribution(call, "success")}', reply_markup=kb.newQuestion(call))
        await bot.send_message(-1001916547261, f'{text.sendQuestions(call, data, "distribution")}', reply_markup=kb.publish(call, id, 'distribution'))
        await state.finish()
    else:
        await bot.send_message(call.from_user.id, f'{text.start(call)}', reply_markup=kb.menu(call))
        await state.finish()