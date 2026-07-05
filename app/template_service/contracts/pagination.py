import typing
from pydantic import BaseModel, Field

T = typing.TypeVar("T")


class Pagination(BaseModel):
    """Pagination details"""
    page: int
    """Page number returned"""

    size: int
    """Size of the returned records"""

    total: int
    """Total available records"""


class PagedResponse(BaseModel, typing.Generic[T]):
    """Generic paged response model"""
    items: typing.List[T]
    """Returned items"""

    pagination: Pagination
    """Pagination details"""


class PaginationParameters(BaseModel):
    """
    Pagination Parameters for Requests
    """

    page: int = Field(
        1, ge=1, description="Page number to retrieve, default 1")
    """Page number to retrieve, default 1"""

    page_size: int = Field(
        20, ge=1, description="The maximum number of records to return")
    """The maximum number of records to return"""
