from asaaspy.schemas.bank import BankAccountViewSchema


class TestBankResource:
    def test_get_bank_account_info(self, asaas_svc):
        account_info = asaas_svc.bank.get_account_info()
        assert isinstance(account_info, BankAccountViewSchema)
        assert isinstance(account_info.account, str)
        assert isinstance(account_info.accountDigit, str)
        assert isinstance(account_info.agency, str)

    def test_get_bank_balance(self, asaas_svc):
        balance_info = asaas_svc.bank.get_balance()

        assert isinstance(balance_info.balance, float)
        assert balance_info.balance == 701.79
