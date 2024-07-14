from dataclasses import dataclass
from asaaspy.schemas.base import BaseSchema
from typing import Optional, Literal, List
from enum import Enum
from datetime import date


class BillingType(Enum):
    UNDEFINED = "UNDEFINED"
    BOLETO = "BOLETO"
    CREDIT_CARD = "CREDIT_CARD"
    PIX = "PIX"


@dataclass
class DiscountDetail(BaseSchema):
    value: int
    dueDateLimitDays: int
    type: Literal["FIXED", "PERCENTAGE"]


@dataclass
class InterestDetail(BaseSchema):
    value: float


@dataclass
class FineDetail(BaseSchema):
    value: int
    type: Literal["FIXED", "PERCENTAGE"]


@dataclass
class SplitDetail(BaseSchema):
    walletId: str
    fixedValue: Optional[float] = None
    percentualValue: Optional[float] = None
    totalFixedValue: Optional[float] = None


@dataclass
class CallbackDetail(BaseSchema):
    successUrl: str
    autoRedirect: bool = True


@dataclass
class PaymentCreateSchema(BaseSchema):
    customer: str
    billingType: BillingType
    value: float
    dueDate: date
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


@dataclass
class RefundDetail(BaseSchema):
    dateCreated: date
    status: Literal["PENDING", "CANCELLED", "DONE"]
    value: float
    description: Optional[str] = None
    transactionReceiptUrl: Optional[str] = None


@dataclass
class PaymentViewSchema(BaseSchema):
    object: str
    id: str
    dateCreated: date
    customer: str
    dueDate: str
    value: float
    netValue: float
    billingType: BillingType
    canBePaidAfterDueDate: bool
    paymentLink: Optional[str] = None
    creditDate: Optional[date] = None
    estimatedCreditDate: Optional[date] = None
    lastInvoiceViewedDate: Optional[date] = None
    lastBankSlipViewedDate: Optional[date] = None
    pixTransaction: Optional[str] = None
    status: Literal["PENDING", "RECEIVED", "CONFIRMED", "OVERDUE", "REFUNDED", "RECEIVED_IN_CASH", "REFUND_REQUESTED", "REFUND_IN_PROGRESS", "CHARGEBACK_REQUESTED", "CHARGEBACK_DISPUTE", "AWAITING_CHARGEBACK_REVERSAL", "DUNNING_REQUESTED", "DUNNING_RECEIVED", "AWAITING_RISK_ANALYSIS"] = "PENDING"
    description: Optional[str] = None
    externalReference: Optional[str] = None
    originalValue: Optional[float] = None
    interestValue: Optional[float] = None
    originalDueDate: Optional[date] = None
    paymentDate: Optional[date] = None
    clientPaymentDate: Optional[date] = None
    installmentNumber: Optional[int] = None
    transactionReceiptUrl: Optional[str] = None
    nossoNumero: Optional[str] = None
    invoiceUrl: Optional[str] = None
    bankSlipUrl: Optional[str] = None
    invoiceNumber: Optional[str] = None
    discount: Optional[DiscountDetail] = None
    fine: Optional[FineDetail] = None
    interest: Optional[InterestDetail] = None
    deleted: Optional[bool] = None
    postalService: Optional[bool] = None
    anticipated: Optional[bool] = None
    anticipable: Optional[bool] = None
    refunds: Optional[List[RefundDetail]] = None
    custody: Optional[str] = None,
    canBePaidAfterDueDate: Optional[bool] = None

