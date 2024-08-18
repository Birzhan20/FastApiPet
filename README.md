FastAPI Task Management API

This project is a simple task management API built with FastAPI and SQLAlchemy. It demonstrates the basics of creating a RESTful API with asynchronous database operations using SQLite. The API allows users to perform CRUD operations on tasks, including adding new tasks and retrieving all tasks.

Key Features:

FastAPI: Provides a high-performance, easy-to-use web framework.
SQLAlchemy (Async): Manages the database interactions with async support.
SQLite: A lightweight database for local development and testing.
Pydantic: Validates and handles data serialization with custom schemas.
Asynchronous Processing: Enables non-blocking operations for efficient API response handling.

Project Structure:

TaskOrm: The main database model representing tasks.
TaskRepository: Repository handling database operations.
APIRouter: Manages API routes for task operations.
schemas: Defines data models and validation schemas.

How to Run:

Install dependencies listed in requirements.txt.
Initialize the database by running the app; the necessary tables will be created automatically.
Use the API to add tasks or retrieve a list of all tasks.

This project serves as a foundation for understanding asynchronous API development with FastAPI and can be expanded with additional features like user authentication, more complex data models, or integration with external services.
