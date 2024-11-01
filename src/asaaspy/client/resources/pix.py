from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.pix import (
    PixKeyFilterBy,
    PixKeyViewSchema,
    StaticQRCodeSchema,
    StaticQRCodeViewSchema,
)


class PixResource(AsaasResource):
    def list_keys(self, **filter_by):
        pix_key_filters = PixKeyFilterBy(**filter_by)
        return self.get_list_response(
            self.call(
                "GET", "v3/pix/addressKeys", params=pix_key_filters.as_lean_dict()
            ),
            PixKeyViewSchema,
        )

    def get_key_by_id(self, id: str) -> PixKeyViewSchema:
        response = self.call("GET", f"v3/pix/addressKeys/{id}")
        return PixKeyViewSchema(**response)

    def delete_key(self, id: str) -> PixKeyViewSchema:
        response = self.call("DELETE", f"v3/pix/addressKeys/{id}")
        return PixKeyViewSchema(**response)

    def create_random_key(self) -> PixKeyViewSchema:
        response = self.call("POST", "v3/pix/addressKeys", json={"type": "EVP"})
        return PixKeyViewSchema(**response)

    def create_qrcode(self, qrcode: StaticQRCodeSchema) -> StaticQRCodeViewSchema:
        response = self.call(
            "POST", "v3/pix/qrCodes/static", json=qrcode.as_lean_dict()
        )
        return StaticQRCodeViewSchema(**response)

    def delete_qrcode(self, id): ...  # noqa E704

    # Transacoes PIX
    def pay_qrcode(self, id): ...  # noqa E704

    def decode_qrcode(self, id): ...  # noqa E704

    def get_transaction(self, id): ...  # noqa E704

    def get_transactions(self): ...  # validate (sounds like Transaction)  # noqa E704

    def cancel_scheduled_transaction(self, id): ...  # noqa E704
