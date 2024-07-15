from asaaspy.client.base import AsaasClient
from asaaspy.client.resources.customer import CustomerResource
from asaaspy.client.resources.payment import PaymentResource


class AsaasService:
    def __init__(self, *args, **kwargs) -> None:
        """
        Inits a new AsaasPy Server instance.

        params:
            api_key(str): Asaas API Key to be used - required
            sandbox(bool): whether use or not sandbox (default False)
        """
        client = AsaasClient(*args, **kwargs)

        self.customer: CustomerResource = CustomerResource(client)
        self.payment: PaymentResource = PaymentResource(client)
