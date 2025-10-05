from sqlmodel import SQLModel, create_engine  # noqa: F401

from server.config import settings

engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    echo=settings.DATABASE_ECHO,
)
