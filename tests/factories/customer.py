import factory

from asaaspy.schemas.customer import CustomerCreateSchema


class CustomerCreateSchemaFactory(factory.Factory):
    class Meta:
        model = CustomerCreateSchema

    name = factory.Faker("name")
    cpfCnpj = factory.Faker("cpf", locale="pt_BR")
