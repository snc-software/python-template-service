from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference, Theme, DocumentDownloadType

from .infrastructure.postgres.connection_factory import init_engine, close_engine

from . import routes
from .infrastructure.logging import configure_logging
from .openapi import open_api_tags as OAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    await init_engine()
    yield
    await close_engine()

app = FastAPI(
    title="Template Service API",
    description="Template Service API",
    version="1.0.0",
    openapi_tags=OAPI.ALL_TAGS,
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan
)


@app.get("/docs", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
        dark_mode=True,
        theme=Theme.MOON,
        show_developer_tools="never",
        show_sidebar=True,
        document_download_type=DocumentDownloadType.JSON,
        telemetry=False,
    )


for router in routes.routers:
    app.include_router(router)
