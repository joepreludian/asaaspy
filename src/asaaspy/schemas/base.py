from datetime import date
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict


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


class PaginatedOutputPayload(BaseSchema):
    object: str
    hasMore: bool
    totalCount: int
    limit: int
    offset: int
    data: Any


class QueryParamsPayload(BaseSchema):
    offset: Optional[int] = None
    limit: Optional[int] = None
