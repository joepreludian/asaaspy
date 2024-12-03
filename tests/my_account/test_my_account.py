from asaaspy.schemas.v3.my_account import MyAccountDocumentsViewSchema


class TestMyAccountResource:
    def test_my_account_get_documents(self, asaas_svc):
        return_data = asaas_svc.my_account.get_pending_documents()
        assert isinstance(return_data, MyAccountDocumentsViewSchema)
