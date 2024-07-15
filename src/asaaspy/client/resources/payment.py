from asaaspy.client.base import AsaasResource
from asaaspy.schemas.base import PaginatedOutputPayload
from asaaspy.schemas.payment import (
    PaymentCreateSchema,
    PaymentFilterBy,
    PaymentViewSchema,
)


class PaymentResource(AsaasResource):
    def create(self, payment: PaymentCreateSchema) -> PaymentViewSchema:
        with self.get_client() as client:
            response = client.post("/v3/payments", json=payment.as_lean_dict())
            return PaymentViewSchema(**response.json())

    def get(self, payment_id) -> PaymentViewSchema:
        with self.get_client() as client:
            response = client.get(f"/v3/payments/{payment_id}")
            return PaymentViewSchema(**response.json())

    def all(self, filter_by: PaymentFilterBy = None) -> PaginatedOutputPayload:
        with self.get_client() as client:
            response = self.get_list_response(
                client.get(
                    "v3/payments",
                    params=filter_by.as_lean_dict() if filter_by else None,
                ),
                data_response_class=PaymentViewSchema,
            )
            return response

    def delete(self, payment_id) -> bool:
        with self.get_client() as client:
            response = client.delete(f"v3/payments/{payment_id}").json()
            return response.get("deleted", False)
