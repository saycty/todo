from sqlalchemy.orm import Session
from . import models, schemas


def get_todos(db: Session) -> list[schemas.ToDoResponse]:
    """
    Retrieve all todos from the database.

    :param db: The database session.
    :return: A list of all todos.
    """
    return db.query(models.ToDo).all()


def get_todo_by_id(db: Session, todo_id: int) -> schemas.ToDoResponse | None:
    """
    Retrieve a todo by its ID.

    :param db: The database session.
    :param todo_id: The ID of the todo to retrieve.
    :return: The todo with the given ID, or None if no such todo exists.
    """
    return db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()


def create_todo(db: Session, todo: schemas.ToDoCreate) -> schemas.ToDoResponse:
    """
    Create a new todo.

    :param db: The database session.
    :param todo: The new todo to create.
    :return: The newly created todo.
    """
    db_todo = models.ToDo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(
    db: Session, todo_id: int, todo: schemas.ToDoUpdate
) -> schemas.ToDoResponse | None:
    """
    Update an existing todo.

    :param db: The database session.
    :param todo_id: The ID of the todo to update.
    :param todo: The new values for the todo.
    :return: The updated todo, or None if no such todo exists.
    """
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        for key, value in todo.dict(exclude_unset=True).items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int) -> schemas.ToDoResponse | None:
    """
    Delete a todo by its ID.

    :param db: The database session.
    :param todo_id: The ID of the todo to delete.
    :return: The deleted todo, or None if no such todo exists.
    """
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo

