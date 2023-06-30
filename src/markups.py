from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.logging_system import logger
from src.yaml_reader import YamlReader


yaml_reader = YamlReader(logger=logger)


def get_start_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    accept_task = InlineKeyboardButton(text=yaml_reader.get_accept_task_button(), callback_data='accept_task')
    refuse_task = InlineKeyboardButton(text=yaml_reader.get_refuse_task_button(), callback_data='refuse_task')
    markup.add(accept_task, refuse_task)
    return markup
