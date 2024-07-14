from typing import Any, Optional
from enum import Enum
from dataclasses import asdict, dataclass
from abc import ABC
from datetime import date


class BaseSchema(ABC):
    def as_dict(self):
        return asdict(self)
    
    def as_lean_dict(self):
        def get_json_value(value):
            if isinstance(value, Enum):
                return value.value
            
            if isinstance(value, date):
                return value.strftime("%Y-%m-%d")

            return value

        return asdict(self, dict_factory=lambda x: {k: get_json_value(v) for (k, v) in x if v is not None})


@dataclass
class PaginatedOutputPayload:
    object: str
    hasMore: bool
    totalCount: int
    limit: int
    offset: int
    data: Any


@dataclass
class QueryParamsPayload(BaseSchema):
    offset: Optional[int] = None
    limit: Optional[int] = None
