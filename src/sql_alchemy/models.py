from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, Text, Boolean


# define declarative Base:
__Base__ = declarative_base()


class Users(__Base__):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer(), nullable=False)
    username = Column(Text(), nullable=False)
    first_name = Column(Text(), nullable=False)
    last_name = Column(Text(), nullable=False)
    have_active_task = Column(Boolean(), nullable=False)
    completed_tasks_count = Column(Integer(), nullable=False)
