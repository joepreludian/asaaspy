# Quickstart

Para utilizar o projeto, voce pode instalá-lo por meio do PIP.

## Instalando
```bash
$ pip install asaaspy
```

## Criando um Cliente e realizando uma cobrança
Condensarei um exemplo simples da utilização dessa biblioteca.

``` py
from asaaspy import AsaasService
from asaaspy.schemas.customer import CustomerCreateSchema
from asaaspy.schemas.payment import PaymentCreateSchema, BillingType

service = AsaasService("ASAAS_API_KEY")
new_customer = service.customer.create(
    CustomerCreateSchema(name="Joao da Silva", cpfCnpj="111.111.111-11")
)

payment = service.payment.create(
    PaymentCreateSchema(
        customer=new_customer.id,
        billingType=BillingType.PIX,
        value=12.34,
        dueDate=date(year=2024, month=7, day=19)
    ))

print(payment.id)

# Experimente usar o autocomplete em `payment` na sua IDE favorita para todas as opções disponíveis. =)
```