from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any
from ..database.session import get_session
from ..models.user import UserCreate, UserRead
from ..services.auth import AuthService
from ..middleware.jwt_auth import JWTBearer

router = APIRouter(prefix="/api/auth", tags=["authentication"])


@router.post("/register", response_model=Dict[str, Any])
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    """
    Register a new user account
    """
    try:
        # Register the user
        db_user = AuthService.register_user(session, user_data)

        # Create access token
        access_token = AuthService.create_access_token_for_user(db_user)

        return {
            "success": True,
            "message": "Registration successful",
            "token": access_token
        }
    except ValueError as e:
        # Email already exists
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"error": "Conflict", "message": str(e)}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "Internal Server Error", "message": "An unexpected error occurred"}
        )


@router.post("/login", response_model=Dict[str, Any])
def login(email: str, password: str, session: Session = Depends(get_session)):
    """
    Authenticate user and return JWT token
    """
    user = AuthService.authenticate_user(session, email, password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": "Unauthorized", "message": "Invalid credentials"}
        )

    # Create access token
    access_token = AuthService.create_access_token_for_user(user)

    return {
        "success": True,
        "message": "Login successful",
        "token": access_token
    }


@router.post("/logout", dependencies=[Depends(JWTBearer())])
def logout():
    """
    Logout user (invalidate session)
    """
    # With JWT tokens, the client typically just discards the token
    # In a real implementation, you might add tokens to a blacklist
    return {
        "success": True,
        "message": "Logged out successfully"
    }