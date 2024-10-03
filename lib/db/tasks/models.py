from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from lib.db.db_controller import Base, int_pk, creation_datetime_at


class Tasks(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    description: Mapped[str]
    priority: Mapped[str]
    creation_datetime: Mapped[creation_datetime_at]
    deadline: Mapped[datetime]
    done: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id},"
            f"name={self.name!r}"
        )

    def __repr__(self):
        return str(self)