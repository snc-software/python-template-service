from typing import List, Optional
from uuid import UUID

from ....infrastructure.postgres.persistence_controller import PersistenceController
from .template_entities import Template


async def get_by_id(
    pc: PersistenceController, template_id: UUID
) -> Optional[Template]:
    row = await pc.query_single_or_default(
        """
        SELECT "Id", "Name", "CreatedTimestamp", "UpdatedTimestamp", "Deleted"
        FROM public."Templates"
        WHERE "Id" = :template_id AND "Deleted" = False
        """,
        {"template_id": template_id},
    )
    return Template(**row) if row else None


async def get_all(
    pc: PersistenceController, limit: int, offset: int
) -> List[Template]:
    rows = await pc.query(
        """
        SELECT "Id", "Name", "CreatedTimestamp", "UpdatedTimestamp", "Deleted"
        FROM public."Templates"
        WHERE "Deleted" = False
        LIMIT :limit OFFSET :offset
        """,
        {"limit": limit, "offset": offset},
    )
    return [Template(**row) for row in rows]


async def count(pc: PersistenceController) -> int:
    row = await pc.query_single(
        """
        SELECT COUNT(*) AS total FROM public."Templates" WHERE "Deleted" = FALSE
        """
    )
    return int(row["total"])
