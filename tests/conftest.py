import pytest
from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from server.config import settings

# Imports all our models for create_all()
from server.database import *  # noqa: F403


@pytest.fixture(scope="session")
def engine_fixture():
    engine = create_engine(
        settings.database_url,
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture(autouse=True)
def session(engine_fixture: Engine):
    with Session(engine_fixture) as session:
        yield session
        session.rollback()
