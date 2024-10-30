from typing import Literal, Optional

from asaaspy.schemas.base import BaseSchema
from asaaspy.schemas.base_fields import Date, DateTime


class QRCodeViewSchema(BaseSchema):
    encodedImage: str
    payload: str


class PixKeyViewSchema(BaseSchema):
    id: str
    key: str
    type: str
    status: Literal["WAITING_ACTIVATION", "ACTIVE", "AWAITING_DELETION", "AWAITING_ACCOUNT_DELETION", "DELETED", "ERROR"]
    dateCreated: DateTime
    canBeDeleted: bool
    cannotBeDeletedReason: Optional[str]
    qrCode: QRCodeViewSchema
