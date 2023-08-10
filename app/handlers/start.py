from app.imports import *

@dp.message_handler()
async def start(message: types.Message):
    user = db.getUsersExist(message.from_user.id)
    if str(user) in 'False':
        db.addUser(message.from_user.id, message.from_user.full_name)

    await bot.send_message(message.chat.id, f'{text.start(message)}', reply_markup=kb.menu(message))

