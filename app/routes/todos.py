from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas import TodoCreate, TodoOut, TodoUpdate
from ..auth import get_current_user

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", response_model=List[TodoOut])
def list_todos(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    todos = (
        db.query(models.Todo)
        .filter(models.Todo.owner_id == current_user.id)
        .order_by(models.Todo.id.desc())
        .all()
    )
    return todos


@router.post("/", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo(
    todo_data: TodoCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    todo = models.Todo(
        title=todo_data.title,
        description=todo_data.description,
        owner_id=current_user.id,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@router.patch("/{todo_id}", response_model=TodoOut)
def update_todo(
    todo_id: int,
    update_data: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    todo = (
        db.query(models.Todo)
        .filter(
            models.Todo.id == todo_id,
            models.Todo.owner_id == current_user.id,
        )
        .first()
    )

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found.",
        )

    if update_data.title is not None:
        todo.title = update_data.title
    if update_data.description is not None:
        todo.description = update_data.description
    if update_data.completed is not None:
        todo.completed = update_data.completed

    db.commit()
    db.refresh(todo)
    return todo
