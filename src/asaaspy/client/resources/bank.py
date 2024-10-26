from asaaspy.client.base import AsaasResource
from asaaspy.schemas.bank import BankAccountViewSchema, BankBalanceViewSchema


class BankResource(AsaasResource):
    def get_account_info(self) -> BankAccountViewSchema:
        response = self.call("GET", "v3/myAccount/accountNumber")
        return BankAccountViewSchema(**response)

    def get_account(self): ...  # noqa E704

    def get_balance(self):
        response = self.call("GET", "v3/finance/balance")
        return BankBalanceViewSchema(**response)

    def get_transactions(self): ...  # noqa E704
