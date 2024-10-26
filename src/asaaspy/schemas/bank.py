from asaaspy.schemas.base import BaseSchema


class BankAccountViewSchema(BaseSchema):
    agency: str
    account: str
    accountDigit: str


class BankBalanceViewSchema(BaseSchema):
    balance: float
