from asaaspy.client.base import AsaasResource
from asaaspy.schemas.customer import (
    CustomerCreateSchema,
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
        with self.get_client() as client:
            response = self.get_list_response(
                client.get(
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
        with self.get_client() as client:
            response = client.get(f"v3/customers/{customer_id}")
            return CustomerViewSchema(**response.json())

    def create(self, customer: CustomerCreateSchema) -> CustomerViewSchema:
        with self.get_client() as client:
            response = client.post("v3/customers", json=customer.as_lean_dict())
            return CustomerViewSchema(**response.json())

    def delete(self, id: str) -> bool:
        with self.get_client() as client:
            response = client.delete(f"v3/customers/{id}").json()
            return response.get("deleted", False)
