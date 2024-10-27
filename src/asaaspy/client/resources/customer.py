from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.customer import (
    CustomerSchema,
    CustomerSearchParams,
    CustomerViewSchema,
)


class CustomerResource(AsaasResource):
    def all(
        self,
        name=None,
        email=None,
        cpf_cnpj=None,
        group_name=None,
        external_reference=None,
        **kwargs,
    ):
        response = self.get_list_response(
            self.call(
                "GET",
                "v3/customers",
                params=CustomerSearchParams(
                    **{
                        "name": name,
                        "email": email,
                        "cpfCnpj": cpf_cnpj,
                        "groupName": group_name,
                        "externalReference": external_reference,
                        **kwargs,
                    }
                ).as_lean_dict(),
            ),
            data_response_class=CustomerViewSchema,
        )
        return response

    def get(self, customer_id):
        response = self.call("GET", f"v3/customers/{customer_id}")
        return CustomerViewSchema(**response)

    def create(self, customer: CustomerSchema) -> CustomerViewSchema:
        response = self.call("POST", "v3/customers", json=customer.as_lean_dict())
        return CustomerViewSchema(**response)

    def update(self, customer_id, customer: CustomerSchema) -> CustomerViewSchema:
        response = self.call(
            "PUT", f"v3/customers/{customer_id}", json=customer.as_lean_dict()
        )
        return CustomerViewSchema(**response)

    def delete(self, id: str) -> bool:
        response = self.call("DELETE", f"v3/customers/{id}")
        return response.get("deleted", False)
