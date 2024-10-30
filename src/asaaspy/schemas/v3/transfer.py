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
    effectiveDate: Optional[DateTime] = Field(default=None)
    confirmedDate: Optional[Date] = Field(default=None)
    endToEndIdentifier: Optional[str] = Field(default=None)
    transactionReceiptUrl: Optional[str] = Field(default=None)
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


class BankSchema(BaseSchema):
    code: str


class BankAccountTEDSchema(BaseSchema):
    bank: BankSchema
    ownerName: str
    accountName: Optional[str] = None
    ownerBirthDate: Optional[Date] = None
    cpfCnpj: Optional[str] = None
    agency: Optional[str] = None
    account: Optional[str] = None
    accountDigit: Optional[str] = None
    bankAccountType: Optional[Literal["CONTA_CORRENTE", "CONTA_POUPANCA"]] = None
    ispb: Optional[str] = None


class TransferSchema(BaseSchema):
    value: float
    operationType: Literal["PIX", "TED"] = "PIX"
    pixAddressKey: Optional[str] = None
    pixAddressKeyType: Literal["CPF", "CNPJ", "EMAIL", "PHONE", "EVP"]
    description: Optional[str] = None
    scheduleDate: Optional[Date] = None
    externalReference: Optional[str] = None
    bankAccount: Optional[BankAccountTEDSchema] = None
