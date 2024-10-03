import json
from sqlalchemy import select, insert, delete

from lib.db.db_controller import async_session_maker
from lib.db.tasks.models import Tasks


async def tasks_get() -> json:
    """
    Получение всех тасок из бд
    :return: list[dict]
    """
    async with async_session_maker() as session:
        query = select(Tasks)
        result = await session.execute(query)
        tasks_comp = json.dumps([task.as_dict() for task in result.scalars().all()])
        return tasks_comp


async def task_insert(data: dict) -> dict:
    async with async_session_maker() as session:
        query = insert(Tasks).values(data)
        await session.execute(query)
        await session.commit()
    return {'status': 'success'}


async def task_delete(id_: int) -> dict:
    async with async_session_maker() as session:
        query = delete(Tasks).where(Tasks.id == id_)
        await session.execute(query)
        await session.commit()
    return {'status': 'success'}