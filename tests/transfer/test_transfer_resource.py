from asaaspy.schemas.v3.transfer import TransferItemViewSchema


class TestPaymentResource:
    def test_get_all_payments(self, asaas_svc):
        return_data = asaas_svc.transfer.get_transfers()
        assert isinstance(return_data.data[0], TransferItemViewSchema)
