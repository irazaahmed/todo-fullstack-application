from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker
from ..config import settings

# Create database engine
engine = create_engine(
    settings.database_url,
    echo=settings.debug,  # Set to True to see SQL queries in logs
    pool_pre_ping=True,   # Verify connections before use
)

# Create session factory
get_session = sessionmaker(engine, autocommit=False, autoflush=False)