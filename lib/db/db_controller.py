from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column
from typing import Annotated

from config import get_db_url


DATABASE_URL = get_db_url()
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

int_pk = Annotated[int, mapped_column(primary_key=True)]
creation_datetime_at = Annotated[datetime, mapped_column(server_default=func.now())]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"

    def as_dict(self) -> dict:
        """
        Сериализация экземпляра модели таблицы в словарь
        :return: dict
        """
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns} # noqa
    