from typing import Any, Optional, Sequence

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncConnection


class PersistenceController:
    """
    Persistence context for Unit of Work Pattern
    """

    def __init__(self, connection: AsyncConnection):
        self.connection = connection
        self.transaction = None
        self._committed = False

    async def start_transaction_manually(self) -> None:
        """Ensure that a transaction is open"""
        if self.transaction is None:
            self.transaction = await self.connection.begin()

    async def save_changes(self) -> None:
        """Ensure connection is closed, if transaction is open, commit"""
        if self.transaction is not None:
            await self.transaction.commit()
        await self.connection.close()
        self._committed = True

    async def rollback_and_close(self) -> None:
        """Rollback the transaction and close the connection"""
        if self.transaction is not None:
            await self.transaction.rollback()
        await self.connection.close()

    async def query_single_or_default(
        self, sql: str, parameters: Optional[dict] = None
    ) -> Optional[dict]:
        result = await self.connection.execute(text(sql), parameters or {})
        row = result.mappings().first()
        return dict(row) if row else None

    async def query_single(self, sql: str, parameters: Optional[dict] = None) -> dict:
        result = await self.connection.execute(text(sql), parameters or {})
        return dict(result.mappings().one())

    async def query(self, sql: str, parameters: Optional[dict] = None) -> Sequence[dict]:
        result = await self.connection.execute(text(sql), parameters or {})
        return [dict(row) for row in result.mappings().all()]

    async def execute(self, sql: str, parameters: Optional[dict] = None) -> int:
        await self.start_transaction_manually()
        result = await self.connection.execute(text(sql), parameters or {})
        return result.rowcount

    async def execute_with_results(
        self, sql: str, parameters: Optional[dict] = None
    ) -> Sequence[dict]:
        await self.start_transaction_manually()
        result = await self.connection.execute(text(sql), parameters or {})
        return [dict(row) for row in result.mappings().all()]

    async def execute_with_result(self, sql: str, parameters: Optional[dict] = None) -> dict:
        await self.start_transaction_manually()
        result = await self.connection.execute(text(sql), parameters or {})
        return dict(result.mappings().one())

    async def dispose(self) -> None:
        if not self._committed and self.transaction is not None:
            await self.transaction.rollback()
        await self.connection.close()

    async def __aenter__(self) -> "PersistenceController":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.dispose()
