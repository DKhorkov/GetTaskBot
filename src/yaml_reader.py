import logging
import os
import yaml

from pathlib import PurePath


class YamlReader:

    def __init__(self, logger: logging.Logger):
        self.__logger = logger
        self.__yaml_configs_dir = PurePath(os.getcwd()) / 'src/yaml_configs/'
        self.__text_templates_yaml = self.__yaml_configs_dir / 'text_templates.yaml'
        self.__markup_buttons_yaml = self.__yaml_configs_dir / 'markup_buttons.yaml'

    def get_start_text(self):
        text_templates = self.__get_text_templates()
        start_text = text_templates.get('start_text')
        return start_text

    def __get_text_templates(self) -> dict:
        with open(self.__text_templates_yaml, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)

        text_templates = yaml_data.get('TEXT_TEMPLATES')
        return text_templates

    def get_accept_task_button(self):
        markup_buttons = self.__get_markup_buttons()
        accept_task_button = markup_buttons.get('accept_task_button')
        return accept_task_button

    def get_refuse_task_button(self):
        markup_buttons = self.__get_markup_buttons()
        accept_task_button = markup_buttons.get('refuse_task_button')
        return accept_task_button

    def __get_markup_buttons(self) -> dict:
        with open(self.__markup_buttons_yaml, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)

        markup_buttons = yaml_data.get('MARKUP_BUTTONS')
        return markup_buttons
