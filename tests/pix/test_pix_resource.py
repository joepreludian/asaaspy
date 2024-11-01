import pytest

from asaaspy.exceptions import AsaasClientError
from asaaspy.schemas.v3.pix import (
    PixKeyViewSchema,
    StaticQRCodeSchema,
    StaticQRCodeViewSchema,
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
