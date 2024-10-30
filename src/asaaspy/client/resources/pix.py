from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.pix import PixKeyViewSchema


class PixResource(AsaasResource):
    def list_keys(self):
        return self.get_list_response(self.call("GET", "v3/pix/addressKeys"), PixKeyViewSchema)

    def get_key_by_id(self, id):
        ...

    def delete_key(self, id):
        ...

    def create_qrcode(self):
        ...

    def delete_qrcode(self, id):
        ...

    # Transacoes PIX
    def pay_qrcode(self, id):
        ...

    def decode_qrcode(self, id):
        ...

    def get_transaction(self, id):
        ... # validate (sounds like Transaction)

    def get_transactions(self):
        ... # validate (sounds like Transaction)

    def cancel_scheduled_transaction(self, id):
        ...