from typing import Optional, Literal, List

from asaaspy.schemas.base import BaseSchema


class ResponsibleSchema(BaseSchema):
    name: str
    type: Literal[
        "ALLOW_BANK_ACCOUNT_DEPOSIT_STATEMENT",
        "ASAAS_ACCOUNT_OWNER_EMANCIPATION_AGE",
        "ASAAS_ACCOUNT_OWNER",
        "ASSOCIATION",
        "BANK_ACCOUNT_OWNER_EMANCIPATION_AGE",
        "BANK_ACCOUNT_OWNER",
        "CUSTOM",
        "DIRECTOR",
        "INDIVIDUAL_COMPANY",
        "LIMITED_COMPANY",
        "MEI",
        "PARTNER",
    ]


class AccountDocumentDetail(BaseSchema):
    id: str
    status: Literal["NOT_SENT", "PENDING", "APPROVED", "REJECTED"]


class AccountDocument(BaseSchema):
    id: Optional[str] = None
    status: Optional[
        Literal["NOT_SENT", "PENDING", "APPROVED", "REJECTED", "IGNORED"]
    ] = None
    type: Optional[
        Literal[
            "IDENTIFICATION",
            "SOCIAL_CONTRACT",
            "ENTREPRENEUR_REQUIREMENT",
            "MINUTES_OF_ELECTION",
            "CUSTOM",
            "IDENTIFICATION_SELFIE",
        ]
    ] = None
    title: Optional[str] = None
    description: Optional[str] = None
    responsible: Optional[ResponsibleSchema] = None
    onboardingUrl: Optional[str] = None
    documents: Optional[List[AccountDocumentDetail]] = None


class MyAccountDocumentsViewSchema(BaseSchema):
    rejectReasons: Optional[str] = None
    data: List[AccountDocument]


class MyAccountSendDocumentViewSchema(BaseSchema):
    id: str
    status: Literal["NOT_SENT", "PENDING", "APPROVED", "REJECTED"]


class MyAccountStatusViewSchema(BaseSchema):
    id: str
    commercialInfo: Literal["PENDING", "APPROVED", "REJECTED", "AWAITING_APPROVAL"]
    bankAccountInfo: Literal["PENDING", "APPROVED", "REJECTED", "AWAITING_APPROVAL"]
    documentation: Literal["PENDING", "APPROVED", "REJECTED", "AWAITING_APPROVAL"]
    general: Literal["PENDING", "APPROVED", "REJECTED", "AWAITING_APPROVAL"]


class MyAccountCloseViewSchema(BaseSchema):
    observations: Optional[str] = None
