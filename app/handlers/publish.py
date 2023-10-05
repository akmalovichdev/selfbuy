from app.imports import *

@dp.callback_query_handler(lambda c: c.data.startswith('publish'))
async def publish(call: types.CallbackQuery):
    await other.deleteMessage(call.message.chat.id, call.message.message_id)

    db.updatepurchase(call.data.split("-")[1], call.data.split("-")[2])

    await bot.send_message(db.selectConf('channel'), f'{text.publish(call.data.split("-")[1], call.data.split("-")[2])}')