from datetime import datetime

from sqlalchemy.orm import Mapped

from lib.db.db_controller import Base, int_pk


class Tasks(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    description: Mapped[str]
    priority: Mapped[str]
    creation_datetime: Mapped[datetime]
    deadline: Mapped[datetime]
    done: Mapped[bool]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id},"
            f"name={self.name!r}"
        )

    def __repr__(self):
        return str(self)