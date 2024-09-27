from sqlalchemy import Column, Integer, String, Boolean, DateTime
from lib.todo_list.db.db_controller import Base


class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(
        Integer(),
        primary_key=True,
        autoincrement=True,
    )
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    priority = Column(String(), nullable=False)
    creation_datetime = Column(DateTime(), nullable=False)
    deadline = Column(DateTime(), nullable=False)
    done = Column(Boolean(), nullable=False)
