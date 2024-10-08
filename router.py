from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post('')
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)  # Добавление задачи в репозиторий
    return {'ok': True, "task_id": task_id}       # Возвращение результата


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()  # Получение всех задач
    return tasks                             # Возвращение списка задач
