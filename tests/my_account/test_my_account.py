from asaaspy.schemas.v3.my_account import (
    MyAccountDocumentsViewSchema,
    MyAccountStatusViewSchema,
)


class TestMyAccountResource:
    def test_my_account_get_documents_subaccount(self, asaas_svc_subaccount):
        return_data = asaas_svc_subaccount.my_account.get_pending_documents()
        assert isinstance(return_data, MyAccountDocumentsViewSchema)

        file1 = return_data.data[0]
        assert file1.id == "766a9870-4abc-4cce-b618-99f8b8cc9334"
        assert file1.status == "NOT_SENT"
        assert file1.type == "IDENTIFICATION"

    def test_my_account_get_status_subaccount(self, asaas_svc_subaccount):
        return_data = asaas_svc_subaccount.my_account.get_status()
        assert isinstance(return_data, MyAccountStatusViewSchema)
        assert return_data.general == "PENDING"

    def test_my_account_close_1(self, asaas_svc_subaccount):
        return_data = asaas_svc_subaccount.my_account.close_account(
            reason="Fechamento Teste"
        )
        assert return_data.observations == "Conta desabilitada com sucesso."
