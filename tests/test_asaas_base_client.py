from asaaspy.service import AsaasService
from asaaspy.service import CustomerResource
 

class TestAsaasBaseClient:
    def test_customer_new(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        assert isinstance(asaas_svc.customer, CustomerResource)
