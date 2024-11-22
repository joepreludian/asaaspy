from typing import Optional, Literal, List
from asaaspy.schemas.base import BaseSchema
from asaaspy.schemas.base_fields import DateTime, Date
from asaaspy.schemas.base import PaginatedQueryParams


class WebhookSchema(BaseSchema):
    apiVersion: Optional[int] = 3
    sendType: Literal["SEQUENTIALLY", "NON_SEQUENTIALLY"] = "SEQUENTIALLY"
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None
    enabled: Optional[bool] = None
    interrupted: Optional[bool] = None
    authToken: Optional[str] = None
    events: Optional[List[str]] = None


class SubAccountSchema(BaseSchema):
    name: str
    email: str
    cpfCnpj: str
    mobilePhone: str
    incomeValue: int
    address: str
    addressNumber: str
    province: str  # Bairro
    postalCode: str
    webhooks: List[WebhookSchema] = []
    companyType: Optional[Literal["MEI", "LIMITED", "INDIVIDUAL", "ASSOCIATION"]] = None
    birthDate: Optional[Date] = None
    loginEmail: Optional[str] = None
    phone: Optional[str] = None
    site: Optional[str] = None
    complement: Optional[str] = None


class SubAccountBankAccountViewSchema(BaseSchema):
    agency: str
    account: str
    accountDigit: str


class SubAccountCommercialInfoExpirationViewSchema(BaseSchema):
    isExpired: Optional[bool]
    scheduledDate: Optional[DateTime]


class SubAccountViewSchema(BaseSchema):
    object: str
    id: str
    name: str
    email: str
    mobilePhone: str
    address: str
    addressNumber: str
    province: str
    postalCode: str
    cpfCnpj: str
    state: str
    walletId: str
    apiKey: Optional[str] = None
    accountNumber: SubAccountBankAccountViewSchema
    loginEmail: Optional[str] = None
    phone: Optional[str] = None
    complement: Optional[str] = None
    birthDate: Optional[str] = None
    personType: Optional[Literal["JURIDICA", "FISICA"]] = None
    companyType: Optional[Literal["MEI", "LIMITED", "INDIVIDUAL", "ASSOCIATION"]] = None
    city: Optional[int] = None
    country: Optional[str] = None
    tradingName: Optional[str] = None
    site: Optional[str] = None
    commercialInfoExpiration: Optional[SubAccountCommercialInfoExpirationViewSchema] = (
        None
    )


class SubAccountFilterBySchema(PaginatedQueryParams):
    cpfCnpj: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    walletId: Optional[str] = None
