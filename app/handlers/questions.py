from app.imports import *
import tracemalloc

tracemalloc.start()

class questionsState(StatesGroup):
    productLink = State()
    purchaseCount = State()
    purchasePurpose = State()
    isProductRetrievalPlanned = State()
    cityForPurchase = State()
    purchaseAlgorithm = State()
    isBuyerRetrievalNeeded = State()
    isReviewNeeded = State()
    isRulesAgreed = State()
    success = State()

@dp.callback_query_handler(text=['questions'])
async def questions(call: types.CallbackQuery, state: FSMContext):
    await other.deleteMessage(call.message.chat.id, call.message.message_id)
    await bot.send_message(call.message.chat.id, f'{text.questions(call, "productLink")}', reply_markup = kb.back())
    await questionsState.purchaseCount.set()

@dp.message_handler(state=questionsState.purchaseCount, content_types=types.ContentType.TEXT)
async def purchaseCount(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(productLink = message.text)
        await message.reply(f'{text.questions(message, "purchaseCount")}', reply_markup = kb.back())
        await questionsState.purchasePurpose.set()

@dp.message_handler(state=questionsState.purchasePurpose, content_types=types.ContentType.TEXT)
async def purchasePurpose(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(purchaseCount = message.text)
        await message.reply(f'{text.questions(message, "purchasePurpose")}', reply_markup = kb.questions(message, "purchasePurpose"))
        await questionsState.isProductRetrievalPlanned.set()

@dp.message_handler(state=questionsState.isProductRetrievalPlanned, content_types=types.ContentType.TEXT)
async def isProductRetrievalPlanned(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(purchasePurpose = message.text)
        await message.reply(f'{text.questions(message, "isProductRetrievalPlanned")}', reply_markup = kb.questions(message, "isProductRetrievalPlanned"))
        await questionsState.cityForPurchase.set()

@dp.message_handler(state=questionsState.cityForPurchase, content_types=types.ContentType.TEXT)
async def cityForPurchase(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(isProductRetrievalPlanned = message.text)
        await message.reply(f'{text.questions(message, "cityForPurchase")}', reply_markup = kb.back())
        await questionsState.purchaseAlgorithm.set()

@dp.message_handler(state=questionsState.purchaseAlgorithm, content_types=types.ContentType.TEXT)
async def purchaseAlgorithm(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(cityForPurchase = message.text)
        await message.reply(f'{text.questions(message, "purchaseAlgorithm")}', reply_markup = kb.back())
        await questionsState.isBuyerRetrievalNeeded.set()

@dp.message_handler(state=questionsState.isBuyerRetrievalNeeded, content_types=types.ContentType.TEXT)
async def isBuyerRetrievalNeeded(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(purchaseAlgorithm = message.text)
        await message.reply(f'{text.questions(message, "isBuyerRetrievalNeeded")}', reply_markup = kb.questions(message, 'isBuyerRetrievalNeeded'))
        await questionsState.isReviewNeeded.set()

@dp.message_handler(state=questionsState.isReviewNeeded, content_types=types.ContentType.TEXT)
async def isReviewNeeded(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(isBuyerRetrievalNeeded = message.text)
        await message.reply(f'{text.questions(message, "isReviewNeeded")}', reply_markup = kb.questions(message, 'isReviewNeeded'))
        await questionsState.isRulesAgreed.set()

@dp.message_handler(state=questionsState.isRulesAgreed, content_types=types.ContentType.TEXT)
async def isRulesAgreed(message: types.Message, state=FSMContext):
    if message.text == 'Отмена':
        # Отмена операции и возврат к стартовому состоянию
        await bot.send_message(message.from_user.id, f'{text.start(message)}', reply_markup=kb.menu(message))
        await state.finish()
    else:        
        await state.update_data(isReviewNeeded = message.text)
        await message.reply(f'{text.questions(message, "isRulesAgreed")}', reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(message.chat.id, f'{text.questions(message, "privacy")}', reply_markup=kb.privacy(message))
        await questionsState.success.set()

@dp.callback_query_handler(state=questionsState.success)
async def callback(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'yes':
        await other.deleteMessage(call.message.chat.id, call.message.message_id)
        data = await state.get_data()
        id = db.addPurchase(call, data, 'questions')
        await bot.send_message(call.from_user.id, f'{text.questions(call, "success")}', reply_markup=kb.newQuestion(call))
        await bot.send_message(-1001916547261, f'{text.sendQuestions(call, data, "questions")}', reply_markup=kb.publish(call, id, 'questions'))
        await state.finish()
    else:
        await bot.send_message(call.from_user.id, f'{text.start(call)}', reply_markup=kb.menu(call))
        await state.finish()