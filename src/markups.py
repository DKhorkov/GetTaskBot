from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.logging_system import logger
from src.yaml_reader import YamlReader


yaml_reader = YamlReader(logger=logger)


def get_start_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    accept_task = InlineKeyboardButton(text=yaml_reader.get_accept_task_button(), callback_data='accept_task')
    refuse_task = InlineKeyboardButton(text=yaml_reader.get_refuse_task_button(), callback_data='refuse_task')
    markup.add(accept_task, refuse_task)
    return markup


def get_accept_task_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    task_completed = InlineKeyboardButton(text=yaml_reader.get_task_completed_button(), callback_data='task_completed')
    markup.add(task_completed)
    return markup


def get_refuse_task_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    task_completed = InlineKeyboardButton(
        text=yaml_reader.get_changed_mind_want_task_button(),
        callback_data='accept_task'
    )
    markup.add(task_completed)
    return markup
