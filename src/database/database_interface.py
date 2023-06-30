from logging import Logger
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.sql import exists
from telebot.types import Message


from src.database.models import __Base__, Users


class DatabaseInterface:

    def __init__(self, logger: Logger) -> None:
        self.__logger = logger
        self.__connection = create_engine(
            "sqlite:///src/database/database.db",
            connect_args={'check_same_thread': False}
        )
        self.__Session_base = sessionmaker(bind=self.__connection)
        self.__session = self.__Session_base()

        self.__create_tables()

    def __create_tables(self) -> None:
        try:
            __Base__.metadata.create_all(self.__connection)
        except InvalidRequestError:
            pass
        except Exception as e:
            self.__logger.error(e)

    def save_user(self, message: Message) -> bool:
        try:
            if not self.__check_if_user_already_registered(user_id=message.from_user.id):
                self.__save_user(message=message)
                return True

            return False
        except Exception as e:
            self.__logger.error(e)

    def __check_if_user_already_registered(self, user_id: int) -> bool:
        user_exists = self.__session.query(exists().where(Users.user_id == user_id)).scalar()
        return user_exists

    def __save_user(self, message: Message) -> None:
        new_user = Users(
            user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name if message.from_user.first_name is not None else 'no name',
            last_name=message.from_user.last_name if message.from_user.last_name is not None else 'no last name',
            have_active_task=False,
            completed_tasks_count=0
        )

        self.__session.add(new_user)
        self.__session.commit()

        self.__logger.info(
            f'User with id={message.from_user.id} and username={message.from_user.username} have subscribed!'
        )
