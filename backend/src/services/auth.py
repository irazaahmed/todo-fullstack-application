from sqlmodel import Session, select
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime
import uuid
from ..models.user import User, UserCreate
from ..middleware.jwt_auth import create_access_token


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    """
    Service class for handling authentication operations
    """

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain password against a hashed password
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        Generate a hash for the given password
        """
        return pwd_context.hash(password)

    @classmethod
    def authenticate_user(cls, session: Session, email: str, password: str) -> Optional[User]:
        """
        Authenticate a user by email and password
        """
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()

        if not user or not cls.verify_password(password, user.hashed_password):
            return None

        return user

    @classmethod
    def register_user(cls, session: Session, user_data: UserCreate) -> User:
        """
        Register a new user
        """
        # Check if user already exists
        existing_user = session.exec(
            select(User).where(User.email == user_data.email)
        ).first()

        if existing_user:
            raise ValueError("Email already registered")

        # Create new user with hashed password
        hashed_password = cls.get_password_hash(user_data.password)
        db_user = User(
            email=user_data.email,
            hashed_password=hashed_password
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user

    @classmethod
    def create_access_token_for_user(cls, user: User) -> str:
        """
        Create an access token for the given user
        """
        return create_access_token(user.id)