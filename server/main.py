import logfire
from fastapi import APIRouter, Depends, FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from hypermedia import Element
from hypermedia.fastapi import full, htmx
from loguru import logger

from server.config import settings
from server.views.index import render_index, render_index_partial

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="My awesome project",
)

logfire.configure()
logfire.instrument_fastapi(app)
logger.configure(handlers=[logfire.loguru_handler()])

logger.info(f"{settings.PROJECT_NAME} starting up!")

insecure_router = APIRouter(
    prefix="",
    tags=["insecure"],
)

secured_router = APIRouter(
    prefix="",
    tags=["secured"],
    dependencies=[],
)


@app.middleware("http")
async def add_vary_accept_header(  # type: ignore
    request: Request,
    call_next,
) -> Response:
    """Add the vary accept header.

    This allows the browser to cache the responses based on caller,
    which prevents the browser from caching htmx responses as a full page
    """
    response: Response = await call_next(request)
    response.headers["Vary"] = "Accept"
    return response


# Insecure endpoints for login
# insecure_router.include_router()


@insecure_router.get("/ping")
async def ping() -> str:
    """Ping the server."""
    return "pong"


@insecure_router.get("/", response_class=HTMLResponse)
@htmx
async def index(
    request: Request,
    partial: Element = Depends(render_index_partial),
    full: Element = Depends(full(render_index)),
) -> None:
    """Return the index page."""
    pass


app.mount("/static", StaticFiles(directory="server/static/"), name="static")
app.include_router(insecure_router)
app.include_router(secured_router)
