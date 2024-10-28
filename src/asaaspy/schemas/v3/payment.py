from datetime import datetime
from enum import Enum
from typing import List, Literal, Optional

from pydantic import Field

from asaaspy.schemas.base import BaseSchema, PaginatedQueryParams, ViewItemSchema
from asaaspy.schemas.base_fields import Date


class BillingType(Enum):
    UNDEFINED = "UNDEFINED"
    BOLETO = "BOLETO"
    CREDIT_CARD = "CREDIT_CARD"
    PIX = "PIX"


class DiscountDetail(BaseSchema):
    value: int
    dueDateLimitDays: int
    type: Literal["FIXED", "PERCENTAGE"]


class InterestDetail(BaseSchema):
    value: float


class FineDetail(BaseSchema):
    value: int
    type: Literal["FIXED", "PERCENTAGE"]


class SplitDetail(BaseSchema):
    walletId: str
    fixedValue: Optional[float] = None
    percentualValue: Optional[float] = None
    totalFixedValue: Optional[float] = None


class CallbackDetail(BaseSchema):
    successUrl: str
    autoRedirect: bool = True


class PaymentCreateSchema(BaseSchema):
    customer: str
    billingType: BillingType
    value: float
    dueDate: Date
    description: Optional[str] = None
    daysAfterDueDateToRegistrationCancellation: Optional[int] = None
    externalReference: Optional[str] = None
    installmentCount: Optional[int] = None
    totalValue: Optional[float] = None
    installmentValue: Optional[float] = None
    discount: Optional[DiscountDetail] = None
    interest: Optional[InterestDetail] = None
    fine: Optional[FineDetail] = None
    postalService: Optional[bool] = None
    split: Optional[List[SplitDetail]] = None
    callback: Optional[CallbackDetail] = None


class RefundDetail(BaseSchema):
    dateCreated: Date
    status: Literal["PENDING", "CANCELLED", "DONE"]
    value: float
    description: Optional[str] = None
    transactionReceiptUrl: Optional[str] = None


class PaymentViewSchema(ViewItemSchema):
    customer: str
    dueDate: Date
    value: float
    netValue: float
    billingType: BillingType
    canBePaidAfterDueDate: bool
    confirmedDate: Optional[Date] = None
    pixQrCodeId: Optional[str] = None
    paymentLink: Optional[str] = None
    creditDate: Optional[Date] = None
    estimatedCreditDate: Optional[Date] = None
    lastInvoiceViewedDate: Optional[datetime] = None
    lastBankSlipViewedDate: Optional[datetime] = None
    pixTransaction: Optional[str] = None
    status: Literal[
        "PENDING",
        "RECEIVED",
        "CONFIRMED",
        "OVERDUE",
        "REFUNDED",
        "RECEIVED_IN_CASH",
        "REFUND_REQUESTED",
        "REFUND_IN_PROGRESS",
        "CHARGEBACK_REQUESTED",
        "CHARGEBACK_DISPUTE",
        "AWAITING_CHARGEBACK_REVERSAL",
        "DUNNING_REQUESTED",
        "DUNNING_RECEIVED",
        "AWAITING_RISK_ANALYSIS",
    ] = "PENDING"
    description: Optional[str] = None
    externalReference: Optional[str] = None
    originalValue: Optional[float] = None
    interestValue: Optional[float] = None
    originalDueDate: Optional[Date] = None
    paymentDate: Optional[Date] = None
    clientPaymentDate: Optional[Date] = None
    installmentNumber: Optional[int] = None
    transactionReceiptUrl: Optional[str] = None
    nossoNumero: Optional[str] = None
    invoiceUrl: Optional[str] = None
    bankSlipUrl: Optional[str] = None
    invoiceNumber: Optional[str] = None
    discount: Optional[DiscountDetail] = None
    fine: Optional[FineDetail] = None
    interest: Optional[InterestDetail] = None
    postalService: Optional[bool] = None
    anticipated: Optional[bool] = None
    anticipable: Optional[bool] = None
    refunds: Optional[List[RefundDetail]] = None
    custody: Optional[str] = (None,)
    canBePaidAfterDueDate: Optional[bool] = None


class PaymentFilterBy(PaginatedQueryParams):
    customer: Optional[str] = None
    customerGroupName: Optional[str] = None
    billingType: Optional[BillingType] = None
    status: Optional[
        Literal[
            "PENDING",
            "RECEIVED",
            "CONFIRMED",
            "OVERDUE",
            "REFUNDED",
            "RECEIVED_IN_CASH",
            "REFUND_REQUESTED",
            "REFUND_IN_PROGRESS",
            "CHARGEBACK_REQUESTED",
            "CHARGEBACK_DISPUTE",
            "AWAITING_CHARGEBACK_REVERSAL",
            "DUNNING_REQUESTED",
            "DUNNING_RECEIVED",
            "AWAITING_RISK_ANALYSIS",
        ]
    ] = None
    subscription: Optional[str] = None
    installment: Optional[str] = None
    externalReference: Optional[str] = None
    paymentDate: Optional[Date] = None
    invoiceStatus: Optional[str] = None
    estimatedCreditDate: Optional[Date] = None
    pixQrCodeId: Optional[str] = None
    anticipated: Optional[bool] = None
    dateCreated_ge: Optional[Date] = Field(
        serialization_alias="dateCreated[ge]", default=None
    )
    dateCreated_le: Optional[Date] = Field(
        serialization_alias="dateCreated[le]", default=None
    )
    paymentDate_ge: Optional[Date] = Field(
        serialization_alias="paymentDate[ge]", default=None
    )
    paymentDate_le: Optional[Date] = Field(
        serialization_alias="paymentDate[le]", default=None
    )
    estimatedCreditDate_ge: Optional[Date] = Field(
        serialization_alias="estimatedCreditDate[ge]", default=None
    )
    estimatedCreditDate_le: Optional[Date] = Field(
        serialization_alias="estimatedCreditDate[le]", default=None
    )
    dueDate_ge: Optional[Date] = Field(serialization_alias="dueDate[ge]", default=None)
    dueDate_le: Optional[Date] = Field(serialization_alias="dueDate[le]", default=None)
    user: Optional[str] = None  # email from user who create the charge
