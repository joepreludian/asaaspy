from typing import Optional
from dataclasses import dataclass
from asaaspy.schemas.base import BaseSchema, QueryParamsPayload


@dataclass
class CustomerCreateSchema(BaseSchema):
    name: str
    cpfCnpj: str
    email: Optional[str] = None
    phone: Optional[str] = None
    mobilePhone: Optional[str] = None
    address: Optional[str] = None
    addressNumber: Optional[str] = None
    complement: Optional[str] = None
    province: Optional[str] = None
    postalCode: Optional[str] = None
    externalReference: Optional[str] = None
    notificationDisabled: Optional[bool] = None
    additionalEmails: Optional[str] = None
    municipalInscription: Optional[str] = None
    stateInscription: Optional[str] = None
    observations: Optional[str] = None
    groupName: Optional[str] = None
    company: Optional[str] = None


@dataclass
class CustomerSchema(CustomerCreateSchema):
    id: Optional[str] = None
    object: Optional[str] = None
    personType: Optional[str] = None
    deleted: Optional[bool] = None
    canDelete: Optional[bool] = None
    canEdit: Optional[bool] = None
    cannotBeDeletedReason: Optional[bool] = None
    cannotEditReason: Optional[str] = None
    dateCreated: Optional[str] = None

    city: Optional[str] = None
    cityName: Optional[str] = None

    state: Optional[str] = None
    country: Optional[str] = None


@dataclass
class CustomerSearchParams(QueryParamsPayload):
    name: Optional[str] = None
    email: Optional[str] = None
    cpfCnpj: Optional[str] = None
    groupName: Optional[str] = None
    externalReference: Optional[str] = None
