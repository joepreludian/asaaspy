from asaaspy.schemas.base import PaginatedViewSchema
from asaaspy.schemas.v3.bank import (
    AccountStatusViewSchema,
    BankAccountViewSchema,
    StatusEnum,
    TransactionItemViewSchema,
)


class TestBankResource:
    def test_get_bank_account_number(self, asaas_svc):
        account_info = asaas_svc.bank.get_account_number()
        assert isinstance(account_info, BankAccountViewSchema)
        assert isinstance(account_info.account, str)
        assert isinstance(account_info.accountDigit, str)
        assert isinstance(account_info.agency, str)

    def test_get_bank_balance(self, asaas_svc):
        balance_info = asaas_svc.bank.get_balance()

        assert isinstance(balance_info.balance, float)
        assert balance_info.balance == 701.79

    def test_get_bank_transactions(self, asaas_svc):
        return_data = asaas_svc.bank.get_transactions()
        assert isinstance(return_data, PaginatedViewSchema)
        assert isinstance(return_data.data[0], TransactionItemViewSchema)

    def test_get_bank_transactions_page_2(self, asaas_svc):
        return_data = asaas_svc.bank.get_transactions(offset=10, limit=10)
        assert isinstance(return_data, PaginatedViewSchema)
        assert isinstance(return_data.data[0], TransactionItemViewSchema)
        assert return_data.hasMore is True

    def test_get_bank_account_status(self, asaas_svc):
        return_data = asaas_svc.bank.get_account_status()
        assert isinstance(return_data, AccountStatusViewSchema)
        assert return_data.general == StatusEnum.PENDING.value
