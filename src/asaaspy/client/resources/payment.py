from asaaspy.client.base import AsaasResource
from asaaspy.schemas.payment import PaymentViewSchema
from asaaspy.schemas.payment import PaymentCreateSchema


class PaymentResource(AsaasResource):
    def create(self, payment: PaymentCreateSchema) -> PaymentViewSchema:
        with self.get_client() as client:
            response = client.post("/v3/payments", json=payment.as_lean_dict())
            return PaymentViewSchema(**response.json())