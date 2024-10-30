import pytest

from asaaspy.schemas.v3.pix import PixKeyViewSchema


class TestPixResource:
    def test_list_keys(self, asaas_svc):
        return_data = asaas_svc.pix.list_keys()
        assert isinstance(return_data.data[0], PixKeyViewSchema)
