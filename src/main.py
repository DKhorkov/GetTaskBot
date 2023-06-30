import telebot

from telebot.types import Message, CallbackQuery
from src.configs import TOKEN
from src.logging_system import logger
from src.database.database_interface import DatabaseInterface
from src.markups import get_start_markup
from src.yaml_reader import YamlReader


bot = telebot.TeleBot(token=TOKEN)
db_interface = DatabaseInterface(logger=logger)
yaml_reader = YamlReader(logger=logger)


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    try:
        new_user = db_interface.save_user(message=message)
        if new_user:
            bot.send_message(
                chat_id=message.chat.id,
                parse_mode='HTML',
                text=yaml_reader.get_start_text(),
                reply_markup=get_start_markup()
            )
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        logger.error(e)


@bot.callback_query_handler(func=lambda call: call.data.startswith('accept_task'))
def accept_task(call: CallbackQuery) -> None:
    try:
        bot.edit_message_reply_markup(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
    except Exception as e:
        logger.error(e)


@bot.callback_query_handler(func=lambda call: call.data.startswith('refuse_task'))
def refuse_task(call: CallbackQuery) -> None:
    try:
        bot.edit_message_reply_markup(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
    except Exception as e:
        logger.error(e)


@bot.callback_query_handler(func=lambda call: call.data.startswith('task_completed'))
def task_completed(call: CallbackQuery) -> None:
    try:
        bot.edit_message_reply_markup(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
    except Exception as e:
        logger.error(e)


@bot.message_handler(
    content_types=[
        'document',
        'audio',
        'video',
        'sticker',
        'video_note',
        'voice',
        'location',
        'contact',
        'animation',
        'dice',
        'poll',
        'text'
])
def dump_messages_handler(message: Message) -> None:
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    except Exception as e:
        logger.error(e)


bot.infinity_polling(timeout=100)
