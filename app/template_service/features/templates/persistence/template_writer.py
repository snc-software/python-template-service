from ....infrastructure.postgres.persistence_controller import PersistenceController
from .template_entities import Template


async def create(
    pc: PersistenceController, template: Template
) -> Template:
    row = await pc.execute_with_result(
        """
        INSERT INTO public."Templates" ("Id", "Name", "CreatedTimestamp", "UpdatedTimestamp", "Deleted")
        VALUES (:id, :name, :created_timestamp, :updated_timestamp, FALSE)
        RETURNING "Id", "Name", "CreatedTimestamp", "UpdatedTimestamp", "Deleted"
        """,
        {
            "id": template.Id,
            "name": template.Name,
            "created_timestamp": template.CreatedTimestamp,
            "updated_timestamp": template.UpdatedTimestamp,
        },
    )
    return Template(**row)
