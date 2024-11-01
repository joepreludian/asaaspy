from typing import Literal, Optional

from asaaspy.schemas.base import BaseSchema, PaginatedQueryParams
from asaaspy.schemas.base_fields import DateTime


class QRCodeViewSchema(BaseSchema):
    encodedImage: str
    payload: str


class PixKeyViewSchema(BaseSchema):
    id: str
    key: str
    type: str
    status: Literal[
        "WAITING_ACTIVATION",
        "ACTIVE",
        "AWAITING_DELETION",
        "AWAITING_ACCOUNT_DELETION",
        "DELETED",
        "ERROR",
    ]
    dateCreated: DateTime
    canBeDeleted: bool
    cannotBeDeletedReason: Optional[str]
    qrCode: QRCodeViewSchema


class PixKeyFilterBy(PaginatedQueryParams):
    status: Optional[
        Literal[
            "AWAITING_ACTIVATION",
            "ACTIVE",
            "AWAITING_DELETION",
            "AWAITING_ACCOUNT_DELETION",
            "DELETED",
            "ERROR",
        ]
    ] = None
    statusList: Optional[str] = None


class StaticQRCodeSchema(BaseSchema):
    addressKey: str
    format: Literal["ALL", "IMAGE", "PAYLOAD"]
    description: Optional[str] = None
    value: Optional[float] = None
    expirationDate: Optional[DateTime] = None
    expirationSeconds: Optional[int] = None
    allowsMultiplePayments: Optional[bool] = None
    externalReference: Optional[str] = None


class StaticQRCodeViewSchema(BaseSchema):
    id: str
    encodedImage: str
    payload: str
    allowsMultiplePayments: Optional[bool] = None
    expirationDate: Optional[DateTime] = None
    externalReference: Optional[str] = None
