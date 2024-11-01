from typing import Literal, Optional

from asaaspy.schemas.base import BaseSchema, PaginatedQueryParams
from asaaspy.schemas.base_fields import DateTime, Date


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


# For Pix Payment
class QRCodePayloadSchema(BaseSchema):
    payload: str
    changeValue: Optional[float] = None


class PixTransactionSchema(BaseSchema):
    qrCode: QRCodePayloadSchema
    value: float
    description: Optional[str] = None
    scheduleDate: Optional[Date] = None


# For view
class PixOriginalTransactionViewSchema(BaseSchema):
    id: str
    value: float
    effectiveDate: Optional[Date] = None
    endToEndIdentifier: Optional[str] = None


class QRCodePayerViewSchema(BaseSchema):
    name: str
    cpfCnpj: str


class QRCodePayExternalAccountViewSchema(BaseSchema):
    ispb: int
    ispbName: Optional[str] = None
    name: Optional[str] = None
    cpfCnpj: Optional[str] = None
    addressKey: Optional[str] = None
    addressKeyType: Optional[Literal["CPF", "CNPJ", "EMAIL", "PHONE", "EVP"]] = None


class QRCodeInfoViewSchema(BaseSchema):
    payer: QRCodePayerViewSchema
    conciliationIdentifier: Optional[str] = None
    originalValue: Optional[float] = None
    dueDate: Optional[Date] = None
    interest: Optional[float] = None
    fine: Optional[float] = None
    discount: Optional[float] = None
    expirationDate: Optional[DateTime] = None


class QRCodePayViewSchema(BaseSchema):
    id: str
    value: float
    status: Literal[
        "AWAITING_BALANCE_VALIDATION",
        "AWAITING_INSTANT_PAYMENT_ACCOUNT_BALANCE",
        "AWAITING_CRITICAL_ACTION_AUTHORIZATION",
        "AWAITING_CHECKOUT_RISK_ANALYSIS_REQUEST",
        "AWAITING_CASH_IN_RISK_ANALYSIS_REQUEST",
        "SCHEDULED",
        "AWAITING_REQUEST",
        "REQUESTED",
        "DONE",
        "REFUSED",
        "CANCELLED",
    ]
    type: Literal[
        "DEBIT", "CREDIT", "CREDIT_REFUND", "DEBIT_REFUND", "DEBIT_REFUND_CANCELLATION"
    ]
    originType: Literal[
        "MANUAL",
        "ADDRESS_KEY",
        "STATIC_QRCODE",
        "DYNAMIC_QRCODE",
        "PAYMENT_INITIATION_SERVICE",
    ]
    endToEndIdentifier: Optional[str] = None
    qrCode: Optional[QRCodeInfoViewSchema] = None
    addressKeyType: Optional[Literal["CPF", "CNPJ", "EMAIL", "PHONE", "EVP"]] = None
    addressKey: Optional[str] = None
    originalTransaction: Optional[PixOriginalTransactionViewSchema] = None
    finality: Optional[Literal["WITHDRAWAL", "CHANGE"]] = None
    externalAccount: Optional[QRCodePayExternalAccountViewSchema] = None
    payment: Optional[str] = None
    canBeRefunded: Optional[bool] = None
    refundDisabledReason: Optional[str] = None
    chargedFeeValue: Optional[float] = None
    dateCreated: Optional[DateTime] = None
    transferId: Optional[str] = None
    externalReference: Optional[str] = None


class PixTransactionsFilterBySchema(PaginatedQueryParams):
    status: Optional[
        Literal[
            "AWAITING_BALANCE_VALIDATION",
            "AWAITING_INSTANT_PAYMENT_ACCOUNT_BALANCE",
            "AWAITING_CRITICAL_ACTION_AUTHORIZATION",
            "AWAITING_CHECKOUT_RISK_ANALYSIS_REQUEST",
            "AWAITING_CASH_IN_RISK_ANALYSIS_REQUEST",
            "SCHEDULED",
            "AWAITING_REQUEST",
            "REQUESTED",
            "DONE",
            "REFUSED",
            "CANCELLED",
        ]
    ] = None
    type: Optional[
        Literal[
            "DEBIT",
            "CREDIT",
            "CREDIT_REFUND",
            "DEBIT_REFUND",
            "DEBIT_REFUND_CANCELLATION",
        ]
    ] = None
    endToEndIdentifier: Optional[str] = None
