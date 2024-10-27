from asaaspy.client.base import AsaasResource
from asaaspy.schemas.base import PaginatedQueryParams
from asaaspy.schemas.v3.bank import (
    AccountStatusViewSchema,
    BankAccountViewSchema,
    BankBalanceViewSchema,
    TransactionItemViewSchema,
)


class BankResource(AsaasResource):
    def get_account_number(self) -> BankAccountViewSchema:
        response = self.call("GET", "v3/myAccount/accountNumber")
        return BankAccountViewSchema(**response)

    def get_account_status(self):
        response = self.call("GET", "v3/myAccount/status")
        return AccountStatusViewSchema(**response)

    def get_balance(self):
        response = self.call("GET", "v3/finance/balance")
        return BankBalanceViewSchema(**response)

    def get_transactions(self, **pagination_kwargs):
        response = self.get_list_response(
            self.call(
                "GET",
                "v3/financialTransactions",
                params=PaginatedQueryParams(**pagination_kwargs).as_lean_dict(),
            ),
            data_response_class=TransactionItemViewSchema,
        )
        return response
