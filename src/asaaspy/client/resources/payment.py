from asaaspy.client.base import AsaasResource
from asaaspy.schemas.payment import PaymentViewSchema
from asaaspy.schemas.payment import PaymentCreateSchema


class PaymentResource(AsaasResource):
    def create(self, payment: PaymentCreateSchema) -> PaymentViewSchema:
        with self.get_client() as client:
            response = client.post("/v3/payments", json=payment.as_lean_dict())
            return PaymentViewSchema(**response.json())
    
    def get(self, payment_id) -> PaymentViewSchema:
        with self.get_client() as client:
            response = client.get(f"/v3/payments/{payment_id}")
            return PaymentViewSchema(**response.json())