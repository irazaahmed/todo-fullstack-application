from sqlmodel import Session, select
from typing import List, Optional
import uuid
from ..models.task import Task, TaskCreate, TaskUpdate
from ..models.user import User


class TaskService:
    """
    Service class for handling task-related operations with user ownership validation
    """

    @classmethod
    def get_user_tasks(cls, session: Session, user_id: uuid.UUID) -> List[Task]:
        """
        Get all tasks for a specific user
        """
        statement = select(Task).where(Task.user_id == user_id)
        return session.exec(statement).all()

    @classmethod
    def get_task_by_id(cls, session: Session, task_id: uuid.UUID, user_id: uuid.UUID) -> Optional[Task]:
        """
        Get a specific task by ID for a specific user (enforces ownership)
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        return session.exec(statement).first()

    @classmethod
    def create_task(cls, session: Session, task_data: TaskCreate, user_id: uuid.UUID) -> Task:
        """
        Create a new task for a specific user
        """
        db_task = Task(**task_data.dict(), user_id=user_id)
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task

    @classmethod
    def update_task(cls, session: Session, task_id: uuid.UUID, task_update: TaskUpdate, user_id: uuid.UUID) -> Optional[Task]:
        """
        Update a task for a specific user (enforces ownership)
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = session.exec(statement).first()

        if not task:
            return None

        # Update task fields
        for field, value in task_update.dict(exclude_unset=True).items():
            setattr(task, field, value)

        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    @classmethod
    def delete_task(cls, session: Session, task_id: uuid.UUID, user_id: uuid.UUID) -> bool:
        """
        Delete a task for a specific user (enforces ownership)
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = session.exec(statement).first()

        if not task:
            return False

        session.delete(task)
        session.commit()
        return True