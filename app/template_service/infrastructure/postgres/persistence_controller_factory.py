from sqlalchemy.ext.asyncio import AsyncEngine

from .persistence_controller import PersistenceController
from .connection_factory import get_engine


async def create_persistence_controller() -> PersistenceController:
    engine = get_engine()
    connection = await engine.connect()
    return PersistenceController(connection)
