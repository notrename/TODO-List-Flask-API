import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Task:
    name: str
    description: str
    priority: str
    deadline: str
    creation_datetime: datetime = datetime.now().strftime('%Y-%m-%d %H:%M')
    done: bool = False
