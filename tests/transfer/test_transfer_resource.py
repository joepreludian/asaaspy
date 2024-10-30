from asaaspy.schemas.v3.transfer import TransferItemViewSchema, TransferSchema


class TestPaymentResource:
    def test_get_all_payments(self, asaas_svc):
        return_data = asaas_svc.transfer.get_transfers()
        assert isinstance(return_data.data[0], TransferItemViewSchema)

    def test_get_transfer_by_id(self, asaas_svc):
        return_data = asaas_svc.transfer.get_by_id(
            "93cbacf4-3bc3-4fd8-802a-f7fdc41922ea"
        )
        assert isinstance(return_data, TransferItemViewSchema)

    def test_create_payment(self, asaas_svc):
        transfer_request = TransferSchema(
            value=100,
            pixAddressKey="cliente-a00005@pix.bcb.gov.br",
            pixAddressKeyType="EMAIL",
        )
        return_data = asaas_svc.transfer.create(transfer_request)
        assert isinstance(return_data, TransferItemViewSchema)

    def test_delete_payment(self, asaas_svc):
        return_data = asaas_svc.transfer.delete(
            id="67049713-a41a-458a-aed4-729babb675ae"
        )
        assert isinstance(return_data, TransferItemViewSchema)
        assert return_data.status == "CANCELLED"
