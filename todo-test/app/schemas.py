from pydantic import BaseModel
from typing import Optional

"""
Schemas to Validate the requests.
"""

class ToDoBase(BaseModel):
    """Base schema for a ToDo item."""
    title: str
    description: Optional[str] = None
    completed: bool = False

class ToDoCreate(ToDoBase):
    """Schema for creating a new ToDo item."""
    pass

class ToDoUpdate(ToDoBase):
    """Schema for updating an existing ToDo item."""
    title: Optional[str] = None
    completed: Optional[bool] = None

class ToDoResponse(ToDoBase):
    """Schema for a ToDo item response with an ID."""
    id: int

    class Config:
        from_attributes = True

