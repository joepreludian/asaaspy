import pytest

from asaaspy.exceptions import AsaasClientError
from asaaspy.schemas.v3.pix import (
    PixKeyViewSchema,
    StaticQRCodeSchema,
    StaticQRCodeViewSchema,
    PixTransactionSchema,
    QRCodePayViewSchema,
)


class TestPixResource:
    def test_list_keys(self, asaas_svc):
        return_data = asaas_svc.pix.list_keys()
        assert isinstance(return_data.data[0], PixKeyViewSchema)

    @pytest.mark.parametrize(
        "status, expected_amount_found", (("ACTIVE", 1), ("DELETED", 0))
    )
    def test_list_keys_with_filters(self, asaas_svc, status, expected_amount_found):
        return_data = asaas_svc.pix.list_keys(status=status)
        assert len(return_data.data) == expected_amount_found

    def test_get_key_by_id(self, asaas_svc):
        return_data = asaas_svc.pix.get_key_by_id(
            "564dbd99-8e86-4342-bafb-c778150a1869"
        )
        assert isinstance(return_data, PixKeyViewSchema)

    def test_create_random_key(self, asaas_svc):
        return_data = asaas_svc.pix.create_random_key()
        assert isinstance(return_data, PixKeyViewSchema)

    def test_create_static_qrcode(self, asaas_svc):
        request = StaticQRCodeSchema(
            addressKey="e3326671-e7d7-40bc-b54d-d8303f8140e8", format="ALL"
        )
        return_data = asaas_svc.pix.create_qrcode(request)
        assert isinstance(return_data, StaticQRCodeViewSchema)

    def test_delete_static_qrcode(self, asaas_svc):
        assert asaas_svc.pix.delete_qrcode("PRELUDIA00000000525658ASA")

    def test_delete_key_by_id_should_trigger_error_400(self, asaas_svc):
        with pytest.raises(AsaasClientError) as exc:
            asaas_svc.pix.delete_key("39006e1e-7c57-4944-ab22-10d957a0d1c9")

        assert exc.value.message == (
            "Sua conta possui autorização crítica habilitada. "
            "Para efetuar esta ação informe o código de confirmação."
        )

    # Payment
    def test_pay_qrcode(self, asaas_svc):
        request = PixTransactionSchema(
            **{
                "qrCode": {
                    "payload": "00020101021226820014br.gov.bcb.pix2560pix-h.asaas.com/qr/cobv/b8eb41f5-468b-4914-8297-662bef42b3f25204000053039865802BR5914Preludian Tech6009Guarulhos61080711500062070503***6304B90E"
                },
                "value": 10,
            }
        )

        response = asaas_svc.pix.pay_qrcode(request)
        assert isinstance(response, QRCodePayViewSchema)

    def test_get_transactions(self, asaas_svc):
        return_data = asaas_svc.pix.get_transactions()
        assert isinstance(return_data.data[0], QRCodePayViewSchema)

    def test_get_transactions_with_filter(self, asaas_svc):
        return_data = asaas_svc.pix.get_transactions(status="DONE")
        assert isinstance(return_data.data[0], QRCodePayViewSchema)

    def test_recover_transaction_by_id(self, asaas_svc):
        return_data = asaas_svc.pix.get_transaction(
            id="693f1933-a522-4c14-9f6e-7cd2c3030ca1"
        )
        assert isinstance(return_data, QRCodePayViewSchema)

    def test_cancel_scheduled_transaction_by_id(self, asaas_svc):
        return_data = asaas_svc.pix.cancel_scheduled_transaction(
            id="693f1933-a522-4c14-9f6e-7cd2c3030ca1"
        )
        assert isinstance(return_data, QRCodePayViewSchema)
        assert return_data.status == "CANCELLED"
