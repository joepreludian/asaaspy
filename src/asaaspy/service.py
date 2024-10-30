from asaaspy.client.base import AsaasHTTPClient
from asaaspy.client.resources.bank import BankResource
from asaaspy.client.resources.customer import CustomerResource
from asaaspy.client.resources.payment import PaymentResource
from asaaspy.client.resources.pix import PixResource
from asaaspy.client.resources.transfer import TransferResource


class AsaasService:
    def __init__(self, *args, **kwargs) -> None:
        """
        Inits a new AsaasPy Server instance.

        params:
            api_key(str): Asaas API Key to be used - required
            sandbox(bool): whether you use or not sandbox (default False)
        """
        client = AsaasHTTPClient(*args, **kwargs)

        self.customer: CustomerResource = CustomerResource(client)
        self.payment: PaymentResource = PaymentResource(client)
        self.bank: BankResource = BankResource(client)
        self.transfer: TransferResource = TransferResource(client)
        self.pix: PixResource = PixResource(client)
