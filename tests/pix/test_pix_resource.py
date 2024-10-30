import pytest

from asaaspy.schemas.v3.pix import PixKeyViewSchema


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
