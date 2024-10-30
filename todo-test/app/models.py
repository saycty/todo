from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class ToDo(Base):
    __tablename__ = "todos"
    """
    Represents a todo item in the database

    Attributes:
        id: The primary key of the todo item
        title: The title of the todo item
        description: The description of the todo item
        completed: Whether the todo item is completed
    """

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
