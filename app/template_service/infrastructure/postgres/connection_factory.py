from typing import Optional

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from ...config import PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DATABASE
from urllib.parse import quote_plus

_engine: Optional[AsyncEngine] = None


def _build_dsn() -> str:
    password = quote_plus(PG_PASSWORD)
    return f"postgresql+asyncpg://{PG_USER}:{password}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"


async def init_engine() -> None:
    global _engine
    _engine = create_async_engine(_build_dsn(), pool_size=5, max_overflow=10)


async def close_engine() -> None:
    global _engine
    if _engine is not None:
        await _engine.dispose()
        _engine = None


def get_engine() -> AsyncEngine:
    if _engine is None:
        raise RuntimeError(
            "Engine not initialized — call init_engine() at startup.")
    return _engine
