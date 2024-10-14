from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# SQLite database for Testing development
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///./{sqlite_file_name}"

connect_args = {"check_same_thread": False}

# Create a new SQLAlchemy engine instance
engine = create_engine(sqlite_url, connect_args=connect_args)

# Create a SessionLocal class that will serve as a factory for session objects
SessionLocal = sessionmaker(
    # Set autocommit to False. This means that each database operation
    # (insert, update, delete) will not be automatically committed.
    # Instead, changes must be explicitly committed with session.commit().
    # This allows for the grouping of multiple operations into a single transaction,
    # ensuring that either all changes are applied or none at all, which helps
    # maintain data integrity.
    autocommit=False,
    # Set autoflush to False. This means that the session will not automatically
    # flush pending changes to the database before executing a query.
    # By disabling autoflush, you have full control over when changes are sent
    # to the database, which can improve performance and prevent unintended
    # behaviors during complex operations.
    # Queries will only see changes after a manual flush or commit is executed.
    autoflush=False,
    # Bind the session to the engine, which specifies the connection
    # to the database defined by the provided database URL.
    bind=engine,
)


Model = declarative_base()

Model.metadata.create_all(engine)


def get_db_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
