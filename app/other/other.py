from app.settings.config import dp, bot

# Функция для удаления сообщений
async def deleteMessage(chat_id, message_id):
    try:
        await bot.delete_message(chat_id, message_id)
    except:
        pass  # Проигнорировать ошибки удаления сообщений