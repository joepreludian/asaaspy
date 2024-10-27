import pytest

from asaaspy.schemas.v3.customer import CustomerSchema, CustomerViewSchema
from asaaspy.service import AsaasService


class TestAsaasGetCustomer:
    def test_get_all_customers(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc
        all_customers = asaas_svc.customer.all()

        assert all_customers.totalCount == 3
        assert isinstance(all_customers.data[0], CustomerViewSchema)

    def test_get_customer(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        CUSTOMER_ID = "cus_000006102042"
        customer = asaas_svc.customer.get(customer_id=CUSTOMER_ID)

        assert customer.id == CUSTOMER_ID

    @pytest.mark.parametrize(
        "extra_params",
        ({"name": "Pedro"}, {"name": "Lucas", "email": "joaodascouves1@gmail.com"}),
    )
    def test_get_all_customers_with_filter(self, asaas_svc, extra_params):
        asaas_svc: AsaasService = asaas_svc

        all_customers = asaas_svc.customer.all()

        assert all_customers.hasMore is False


class TestAsaasCreateCustomer:
    def test_create_customer(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        customer = CustomerSchema(name="Karen Baldwin", cpfCnpj="458.907.623-38")
        new_customer = asaas_svc.customer.create(customer)

        assert new_customer.id is not None

    def test_create_customer_minimal(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        customer = CustomerSchema(name="Empresa Apenas com o nome")
        new_customer = asaas_svc.customer.create(customer)

        assert new_customer.id.startswith("cus_")


class TestAsaasUpdateCustomer:
    def test_update_customer(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        customer = CustomerSchema(name="Karen Rizzo", cpfCnpj="458.907.623-38")
        new_customer = asaas_svc.customer.update(
            customer_id="cus_000006100224", customer=customer
        )

        assert new_customer.id is not None
        assert new_customer.name == "Karen Rizzo"


class TestAsaasDeleteCustomer:
    def test_delete(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        customer = CustomerSchema(
            name="Usuario a Ser Excluido", cpfCnpj="083.138.660-63"
        )
        new_customer = asaas_svc.customer.create(customer)

        has_deleted = asaas_svc.customer.delete(id=new_customer.id)

        assert has_deleted
