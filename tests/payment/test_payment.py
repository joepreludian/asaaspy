from asaaspy.service import AsaasService
from asaaspy.schemas.payment import PaymentCreateSchema, BillingType, PaymentViewSchema
from datetime import date


class TestAsaasPayment:

    def test_create_minimal_payment(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        payment_create = PaymentCreateSchema(
            customer="cus_000006100224",
            billingType=BillingType.PIX,
            value=10.23,
            dueDate=date(year=2024, month=7, day=20)
        )

        payment_details = asaas_svc.payment.create(payment_create)

        assert payment_details.id.startswith("pay_")
        assert isinstance(payment_details, PaymentViewSchema)
