from typing import List, Optional, Tuple
from uuid import UUID

from .. import template_mapper as mapper
from .template_models import TemplateModel
from ....infrastructure.postgres.persistence_controller_factory import create_persistence_controller
from ..persistence import template_reader as reader, template_writer as writer


async def get_by_id(template_id: UUID) -> Optional[TemplateModel]:
    """Fetch a template by its unique identifier"""
    pc = await create_persistence_controller()
    template = await reader.get_by_id(pc, template_id)
    await pc.save_changes()
    return mapper.map_from_persistence_to_domain(template) if template else None


async def get_page(page: int, page_size: int) -> Tuple[List[TemplateModel], int]:
    """Get page of templates"""
    offset = (page - 1) * page_size
    pc = await create_persistence_controller()
    templates = await reader.get_all(pc, limit=page_size, offset=offset)
    total = await reader.count(pc)
    await pc.save_changes()
    return [mapper.map_from_persistence_to_domain(t) for t in templates], total


async def create(template: TemplateModel) -> TemplateModel:
    """Create a new template"""
    persistence_template = mapper.map_from_domain_to_persistence(
        template, False)
    pc = await create_persistence_controller()
    await pc.start_transaction_manually()
    created = await writer.create(pc, persistence_template)
    await pc.save_changes()
    return mapper.map_from_persistence_to_domain(created)
