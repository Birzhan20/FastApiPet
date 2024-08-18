from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()  # Очистка базы данных
    print('База очищена')
    await create_tables()  # Создание таблиц
    print('База готова к работе')
    yield
    print("Выключение")  # Действия при завершении

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)
