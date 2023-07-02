import telebot
import random

from telebot.types import Message, CallbackQuery

from configs import TOKEN
from logging_system import logger
from sql_alchemy.database_interface import DatabaseInterface
from markups import get_start_markup, get_accept_task_markup, get_refuse_task_markup
from yaml_reader import YamlReader


bot = telebot.TeleBot(token=TOKEN)
db_interface = DatabaseInterface(logger=logger)
yaml_reader = YamlReader(logger=logger)
tasks_list = yaml_reader.get_tasks_list()


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

        if len(tasks_list) > 0:
            task_index = random.randint(0, len(tasks_list) - 1)
            task = tasks_list.pop(task_index)
            db_interface.change_active_task_status(user_id=call.from_user.id)
            bot.send_message(
                chat_id=call.from_user.id,
                text=yaml_reader.get_accept_task_text() + task,
                reply_markup=get_accept_task_markup()
            )

        else:
            bot.send_message(
                chat_id=call.from_user.id,
                text=yaml_reader.get_empty_tasks_list_text() + yaml_reader.get_thank_for_participation_text(),
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

        bot.send_message(
            chat_id=call.from_user.id,
            text=yaml_reader.get_refuse_task_text(),
            reply_markup=get_refuse_task_markup()
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

        db_interface.change_active_task_status(user_id=call.from_user.id)
        db_interface.increment_completed_tasks_count(user_id=call.from_user.id)
        bot.send_message(
            chat_id=call.from_user.id,
            text=yaml_reader.get_thank_for_participation_text(),
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
