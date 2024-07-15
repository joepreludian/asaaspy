import datetime

from pydantic import BeforeValidator, PlainSerializer
from typing_extensions import Annotated

Date = Annotated[
    datetime.date,
    BeforeValidator(
        lambda x: datetime.datetime.strptime(x, "%Y-%m-%d") if isinstance(x, str) else x
    ),
    PlainSerializer(lambda x: x.strftime("%Y-%m-%d")),
]
