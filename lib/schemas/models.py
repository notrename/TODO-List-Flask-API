from datetime import datetime

from pydantic import BaseModel, validator, ValidationError


class TaskQuery(BaseModel):
    name: str
    description: str
    priority: str
    deadline: datetime


class TaskDelQuery(BaseModel):
    id: int
