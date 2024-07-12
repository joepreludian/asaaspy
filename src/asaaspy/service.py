from asaaspy.client.base import AsaasClient
from asaaspy.client.customer import CustomerResource


class AsaasService:
    def __init__(self, *args, **kwargs) -> None:
        client = AsaasClient(*args, **kwargs)
        
        self.customer: CustomerResource = CustomerResource(client) 