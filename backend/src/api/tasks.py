from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import List, Dict, Any
import uuid
from ..database.session import get_session
from ..middleware.jwt_auth import JWTBearer
from ..models.task import Task, TaskCreate, TaskRead, TaskUpdate
from ..models.user import User
from ..services.task_service import TaskService

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("/", response_model=Dict[str, List[TaskRead]])
def get_tasks(request: Request, session: Session = Depends(get_session)):
    """
    Retrieve all tasks for the authenticated user
    """
    user_id = getattr(request.state, 'user_id', None)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Unauthorized", "message": "Missing or invalid token"}
        )

    tasks = TaskService.get_user_tasks(session, user_id)
    return {"tasks": tasks}


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(request: Request, task_data: TaskCreate, session: Session = Depends(get_session)):
    """
    Create a new task for the authenticated user
    """
    user_id = getattr(request.state, 'user_id', None)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Unauthorized", "message": "Missing or invalid token"}
        )

    db_task = TaskService.create_task(session, task_data, user_id)
    return db_task


@router.get("/{task_id}", response_model=TaskRead)
def get_task(request: Request, task_id: uuid.UUID, session: Session = Depends(get_session)):
    """
    Retrieve a specific task by ID
    """
    user_id = getattr(request.state, 'user_id', None)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Unauthorized", "message": "Missing or invalid token"}
        )

    task = TaskService.get_task_by_id(session, task_id, user_id)

    if not task:
        # Check if task exists for another user
        other_user_task_exists = session.get(Task, task_id)
        if other_user_task_exists:
            # Task exists but belongs to another user
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"error": "Forbidden", "message": "Access denied - task does not belong to user"}
            )
        else:
            # Task doesn't exist
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": "Not Found", "message": "Task not found"}
            )

    return task


@router.put("/{task_id}", response_model=TaskRead)
def update_task(request: Request, task_id: uuid.UUID, task_update: TaskUpdate, session: Session = Depends(get_session)):
    """
    Update an existing task
    """
    user_id = getattr(request.state, 'user_id', None)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Unauthorized", "message": "Missing or invalid token"}
        )

    updated_task = TaskService.update_task(session, task_id, task_update, user_id)

    if not updated_task:
        # Check if task exists for another user
        other_user_task_exists = session.get(Task, task_id)
        if other_user_task_exists:
            # Task exists but belongs to another user
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"error": "Forbidden", "message": "Access denied - task does not belong to user"}
            )
        else:
            # Task doesn't exist
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": "Not Found", "message": "Task not found"}
            )

    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(request: Request, task_id: uuid.UUID, session: Session = Depends(get_session)):
    """
    Delete a task
    """
    user_id = getattr(request.state, 'user_id', None)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Unauthorized", "message": "Missing or invalid token"}
        )

    deleted = TaskService.delete_task(session, task_id, user_id)

    if not deleted:
        # Check if task exists for another user
        other_user_task_exists = session.get(Task, task_id)
        if other_user_task_exists:
            # Task exists but belongs to another user
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"error": "Forbidden", "message": "Access denied - task does not belong to user"}
            )
        else:
            # Task doesn't exist
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": "Not Found", "message": "Task not found"}
            )

    # Return 204 No Content
    return