import logging
import os
import yaml

from pathlib import PurePath


class YamlReader:

    def __init__(self, logger: logging.Logger) -> None:
        self.__logger = logger
        self.__yaml_configs_dir = PurePath(os.getcwd()) / 'src/yaml_configs/'
        self.__text_templates_yaml = self.__yaml_configs_dir / 'text_templates.yaml'
        self.__markup_buttons_yaml = self.__yaml_configs_dir / 'markup_buttons.yaml'
        self.__tasks_yaml = self.__yaml_configs_dir / 'tasks.yaml'

    def get_start_text(self) -> str:
        text_templates = self.__get_text_templates()
        start_text = text_templates.get('start_text')
        return start_text

    def get_accept_task_text(self) -> str:
        text_templates = self.__get_text_templates()
        accept_task_text = text_templates.get('accept_task_text')
        return accept_task_text

    def get_refuse_task_text(self) -> str:
        text_templates = self.__get_text_templates()
        refuse_task_text = text_templates.get('refuse_task_text')
        return refuse_task_text

    def get_empty_tasks_list_text(self) -> str:
        text_templates = self.__get_text_templates()
        empty_tasks_list_text = text_templates.get('empty_tasks_list_text')
        return empty_tasks_list_text

    def get_thank_for_participation_text(self) -> str:
        text_templates = self.__get_text_templates()
        thank_for_participation_text = text_templates.get('thank_for_participation_text')
        return thank_for_participation_text

    def __get_text_templates(self) -> dict:
        with open(self.__text_templates_yaml, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)

        text_templates = yaml_data.get('TEXT_TEMPLATES')
        return text_templates

    def get_accept_task_button(self) -> str:
        markup_buttons = self.__get_markup_buttons()
        accept_task_button = markup_buttons.get('accept_task_button')
        return accept_task_button

    def get_refuse_task_button(self) -> str:
        markup_buttons = self.__get_markup_buttons()
        accept_task_button = markup_buttons.get('refuse_task_button')
        return accept_task_button

    def get_task_completed_button(self) -> str:
        markup_buttons = self.__get_markup_buttons()
        task_completed_button = markup_buttons.get('task_completed_button')
        return task_completed_button

    def get_changed_mind_want_task_button(self) -> str:
        markup_buttons = self.__get_markup_buttons()
        changed_mind_want_task_button = markup_buttons.get('changed_mind_want_task_button')
        return changed_mind_want_task_button

    def __get_markup_buttons(self) -> dict:
        with open(self.__markup_buttons_yaml, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)

        markup_buttons = yaml_data.get('MARKUP_BUTTONS')
        return markup_buttons

    def get_tasks_list(self) -> list[str]:
        with open(self.__tasks_yaml, 'r') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)

        tasks_list = yaml_data.get('TASKS')
        return tasks_list
