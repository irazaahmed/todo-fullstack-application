from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid
from typing import Optional


class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False, max_length=255)


class User(UserBase, table=True):
    """
    Represents an authenticated user in the system
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Hashed password field
    hashed_password: str = Field(nullable=False, max_length=255)


class UserCreate(UserBase):
    """
    Schema for creating a new user
    """
    password: str = Field(min_length=8, max_length=128)


class UserRead(UserBase):
    """
    Schema for reading user data (without sensitive information)
    """
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime