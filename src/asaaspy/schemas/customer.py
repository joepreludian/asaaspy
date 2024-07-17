from typing import Optional

from asaaspy.schemas.base import BaseSchema, QueryParamsPayload
from asaaspy.schemas.fields import Date


class CustomerCreateSchema(BaseSchema):
    name: str
    cpfCnpj: Optional[str] = None
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


class CustomerViewSchema(CustomerCreateSchema):
    id: Optional[str] = None
    object: Optional[str] = None
    personType: Optional[str] = None
    deleted: Optional[bool] = None
    canDelete: Optional[bool] = None
    canEdit: Optional[bool] = None
    cannotBeDeletedReason: Optional[str] = None
    cannotEditReason: Optional[str] = None
    dateCreated: Optional[Date] = None

    city: Optional[str] = None
    cityName: Optional[str] = None

    state: Optional[str] = None
    country: Optional[str] = None


class CustomerSearchParams(QueryParamsPayload):
    name: Optional[str] = None
    email: Optional[str] = None
    cpfCnpj: Optional[str] = None
    groupName: Optional[str] = None
    externalReference: Optional[str] = None
