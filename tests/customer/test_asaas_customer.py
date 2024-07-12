import pytest
from asaaspy.service import AsaasService
from asaaspy.schemas.customer import CustomerSchema, CustomerCreateSchema
from tests.factories.customer import CustomerCreateSchemaFactory


class TestAsaasGetCustomer:
    def test_get_all_customers(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc
        all_customers = asaas_svc.customer.all()

        assert all_customers.totalCount == 3
        assert isinstance(all_customers.data[0], CustomerSchema)

    @pytest.mark.parametrize('extra_params', (
            {"name": "Pedro"},
            {"name": "Lucas", "email": "joaodascouves1@gmail.com"}
    ))
    def test_get_all_customers_with_filter(self, asaas_svc, extra_params):
        asaas_svc: AsaasService = asaas_svc
        
        all_customers = asaas_svc.customer.all()

        assert all_customers.hasMore is False


class TestAsaasCreateCustomerSchema:
    def test_create_schema_factory(self):
        new_customer = CustomerCreateSchemaFactory()

        assert isinstance(new_customer, CustomerCreateSchema)


class TestAsaasCreateCustomer:
    def test_create_customer(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc
        
        customer = CustomerCreateSchema(name="Karen Baldwin", cpfCnpj="458.907.623-38") 
        new_customer = asaas_svc.customer.create(customer)

        assert new_customer.id is not None