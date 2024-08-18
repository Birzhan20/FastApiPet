from pydantic import BaseModel, ConfigDict


# Схема для добавления задачи
class STaskAdd(BaseModel):
    name: str                    # Имя задачи
    description: str | None      # Описание задачи (может быть None)


# Схема задачи с ID
class STask(STaskAdd):
    id: int                      # Уникальный идентификатор задачи

    # Настройки для извлечения данных из ORM-модели
    model_config = ConfigDict(from_attributes=True)


# Схема для возвращаемого результата при добавлении задачи
class STaskId(BaseModel):
    ok: bool = True              # Статус успеха операции
    task_id: int                 # ID добавленной задачи
