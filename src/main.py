import telebot

from telebot.types import Message
from src.configs import TOKEN, logger
from src.database.database_interface import DatabaseInterface


bot = telebot.TeleBot(token=TOKEN)
db_interface = DatabaseInterface(logger=logger)


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    try:
        new_user = db_interface.save_user(message=message)
        if new_user:
            bot.send_message(
                chat_id=message.chat.id,
                parse_mode='HTML',
                text='You are registered!',
                reply_markup=None
            )
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        logger.error(e)


bot.infinity_polling(timeout=100)
