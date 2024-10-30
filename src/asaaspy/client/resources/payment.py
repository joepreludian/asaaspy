from asaaspy.client.base import AsaasResource
from asaaspy.schemas.base import PaginatedViewSchema
from asaaspy.schemas.v3.payment import (
    PaymentCreateSchema,
    PaymentFilterBy,
    PaymentViewSchema,
)


class PaymentResource(AsaasResource):
    def create(self, payment: PaymentCreateSchema) -> PaymentViewSchema:
        response = self.call("POST", "/v3/payments", json=payment.as_lean_dict())
        return PaymentViewSchema(**response)

    def put(self, payment_id, payment: PaymentCreateSchema) -> PaymentViewSchema:
        response = self.call(
            "PUT", f"/v3/payments/{payment_id}", json=payment.as_lean_dict()
        )
        return PaymentViewSchema(**response)

    def get(self, payment_id) -> PaymentViewSchema:
        response = self.call("GET", f"/v3/payments/{payment_id}")
        return PaymentViewSchema(**response)

    def all(self, **payment_filter_by) -> PaginatedViewSchema:
        filter_by = PaymentFilterBy(**payment_filter_by) if payment_filter_by else None
        response = self.get_list_response(
            self.call(
                "GET",
                "v3/payments",
                params=filter_by.as_lean_dict() if filter_by else None,
            ),
            data_response_class=PaymentViewSchema,
        )
        return response

    def delete(self, payment_id) -> bool:
        response = self.call("DELETE", f"v3/payments/{payment_id}")
        return response.get("deleted", False)
