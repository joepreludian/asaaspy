from typing import Literal, Optional

from pydantic import Field

from asaaspy.schemas.base import BaseSchema, PaginatedQueryParams
from asaaspy.schemas.base_fields import Date, DateTime


class BankDetailViewSchema(BaseSchema):
    name: str
    ispb: str
    code: Optional[str] = None


class BankAccountViewSchema(BaseSchema):
    bank: BankDetailViewSchema
    ownerName: str
    cpfCnpj: str
    type: str
    accountName: Optional[str] = None
    agency: Optional[str] = None
    agencyDigit: Optional[str] = None
    account: Optional[str] = None
    accountDigit: Optional[str] = None
    pixAddressKey: Optional[str] = None


class TransferItemViewSchema(BaseSchema):
    object: str
    id: str
    value: float
    netValue: float
    transferFee: float
    dateCreated: Date
    status: Literal["PENDING", "BANK_PROCESSING", "DONE", "CANCELLED", "FAILED"]
    effectiveDate: DateTime
    confirmedDate: Date
    endToEndIdentifier: str
    transactionReceiptUrl: str
    operationType: Literal["PIX", "TED", "INTERNAL"]
    failReason: Optional[str]
    walletId: Optional[str]
    description: Optional[str]
    canBeCancelled: bool
    externalReference: Optional[str]
    authorized: bool
    scheduleDate: Optional[Date]
    type: str
    bankAccount: BankAccountViewSchema


class TransferFilterBy(PaginatedQueryParams):
    dateCreated_ge: Optional[Date] = Field(
        serialization_alias="dateCreated[ge]", default=None
    )
    dateCreated_le: Optional[Date] = Field(
        serialization_alias="dateCreated[le]", default=None
    )
    transferDate_ge: Optional[Date] = Field(
        serialization_alias="paymentDate[ge]", default=None
    )
    transferDate_le: Optional[Date] = Field(
        serialization_alias="paymentDate[le]", default=None
    )
    type: Optional[str] = None
