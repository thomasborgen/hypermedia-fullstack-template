from typing import Generator

from fastapi import Request
from sqlmodel import Session

from server.database import engine


def get_session() -> Generator[Session, None, None]:
    """Yield FastApi session dependency."""
    with Session(engine) as session:
        yield session


def is_htmx_request(request: Request) -> bool:
    """Is the current request is made by HTMX."""
    return "HX-Request" in request.headers
