from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine,)

app = FastAPI()


def get_db():
    """
    Dependency function that yields a database session.

    This function is used as a dependency for all the endpoints in this API.
    It creates a new database session, yields it, and then closes it.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos", response_model=list[schemas.ToDoResponse])
def read_todos(db: Session = Depends(get_db)):
    """Get all todos.

    Get all todos.

    """
    return crud.get_todos(db)


@app.post("/todos", response_model=schemas.ToDoResponse)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    """Create a new todo.

    Create a new todo.

    """
    return crud.create_todo(db, todo)


@app.get("/todos/{todo_id}", response_model=schemas.ToDoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a single todo by id.

    Get a single todo by id.

    Args:
        todo_id (int): The id of the todo to retrieve.

    Raises:
        HTTPException: If the todo is not found.

    """
    db_todo = crud.get_todo_by_id(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@app.put("/todos/{todo_id}", response_model=schemas.ToDoResponse)
def update_todo(todo_id: int, todo: schemas.ToDoUpdate, db: Session = Depends(get_db)):
    """Update a todo by id.

    Update a todo by id.

    Args:
        todo_id (int): The id of the todo to update.
        todo (schemas.ToDoUpdate): The updated todo data.

    Raises:
        HTTPException: If the todo is not found.

    """
    db_todo = crud.update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@app.delete("/todos/{todo_id}", response_model=schemas.ToDoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo by id.

    Delete a todo by id.

    Args:
        todo_id (int): The id of the todo to delete.

    Raises:
        HTTPException: If the todo is not found.

    """
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo
