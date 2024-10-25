import factory

from asaaspy.schemas.customer import CustomerSchema


class CustomerCreateSchemaFactory(factory.Factory):
    class Meta:
        model = CustomerSchema

    name = factory.Faker("name")
    cpfCnpj = factory.Faker("cpf", locale="pt_BR")
