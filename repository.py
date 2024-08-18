from database import new_session, TaskOrm
from sqlalchemy import select
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()  # Преобразование данных в словарь
            task = TaskOrm(**task_dict)    # Создание ORM объекта
            session.add(task)              # Добавление задачи в сессию
            await session.flush()          # Обновление сессии
            await session.commit()         # Коммит изменений
            return task.id                 # Возвращение ID новой задачи

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)        # Создание запроса
            result = await session.execute(query)  # Выполнение запроса
            task_models = result.scalars().all()   # Извлечение результатов
            task_schemas = [STask.model_validate(task) for task in task_models]  # Валидация
            return task_schemas              # Возвращение списка задач
