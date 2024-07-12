from typing import Dict, Any, Optional
from dataclasses import asdict, dataclass
from abc import ABC


class BaseSchema(ABC):
    def as_dict(self):
        return asdict(self)
    
    def as_lean_dict(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})


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
