from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.pix import PixKeyViewSchema


class PixResource(AsaasResource):
    def list_keys(self):
        return self.get_list_response(
            self.call("GET", "v3/pix/addressKeys"), PixKeyViewSchema
        )

    def get_key_by_id(self, id): ...  # noqa E704

    def delete_key(self, id): ...  # noqa E704

    def create_qrcode(self): ...  # noqa E704

    def delete_qrcode(self, id): ...  # noqa E704

    # Transacoes PIX
    def pay_qrcode(self, id): ...  # noqa E704

    def decode_qrcode(self, id): ...  # noqa E704

    def get_transaction(self, id): ...  # noqa E704

    def get_transactions(self): ...  # validate (sounds like Transaction)  # noqa E704

    def cancel_scheduled_transaction(self, id): ...  # noqa E704
