from datetime import date
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict, Field

from asaaspy.schemas.base_fields import Date


def sanitize_to_json(value):
    if isinstance(value, Enum):
        return value.value

    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")

    return value


class BaseSchema(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    def as_lean_dict(self):
        return self.model_dump(exclude_none=True, by_alias=True)


class PaginatedViewSchema(BaseSchema):
    object: Optional[str] = Field(default=None)
    hasMore: bool
    totalCount: int
    limit: int
    offset: int
    data: Any


class PaginatedQueryParams(BaseSchema):
    offset: Optional[int] = None
    limit: Optional[int] = None


class ViewItemSchema(BaseSchema):
    id: Optional[str] = None
    object: Optional[str] = None
    deleted: Optional[bool] = None
    dateCreated: Optional[Date] = None
