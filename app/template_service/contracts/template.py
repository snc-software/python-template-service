from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class CreateTemplateRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)


class TemplateResponse(BaseModel):
    id: UUID
    name: str
    createdTimestamp: datetime
    updatedTimestamp: datetime
