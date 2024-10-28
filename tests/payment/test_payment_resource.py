from datetime import date

import pytest

from asaaspy.exceptions import AsaasClientError
from asaaspy.schemas.v3.payment import (
    BillingType,
    PaymentCreateSchema,
    PaymentFilterBy,
    PaymentViewSchema,
)
from asaaspy.service import AsaasService


class TestAsaasCreatePayment:
    def test_create_minimal_payment(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        payment_create = PaymentCreateSchema(
            customer="cus_000006100224",
            billingType=BillingType.PIX,
            value=10.23,
            dueDate=date(year=2024, month=7, day=20),
        )

        payment_details = asaas_svc.payment.create(payment_create)

        assert payment_details.id.startswith("pay_")
        assert isinstance(payment_details, PaymentViewSchema)

    def test_create_payment_below_minimum_value(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        payment_create = PaymentCreateSchema(
            customer="cus_000006100224",
            billingType=BillingType.PIX,
            value=3,
            dueDate=date(year=2024, month=10, day=30),
        )

        with pytest.raises(AsaasClientError) as exc_info:
            asaas_svc.payment.create(payment_create)

        assert exc_info.value.message == (
            "O valor da cobrança (R$ 3,00) menos o valor do desconto (R$ 0,00) "
            "não pode ser menor que R$ 5,00."
        )
        assert exc_info.value.status_code == 400
        assert isinstance(exc_info.value.details, dict)


class TestAsaasGetPayment:
    def test_get_payment(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        payment = asaas_svc.payment.get("pay_egd03gp8vsz433au")

        assert payment.id == "pay_egd03gp8vsz433au"
        assert payment.value == 10.23
        assert payment.dueDate == date(year=2024, month=7, day=20)


class TestAsaasPutPayment:
    def test_put_payment(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        payment = asaas_svc.payment.put(
            "pay_atg6n271g1l6nzhm",
            PaymentCreateSchema(
                customer="cus_000006100224",
                billingType=BillingType.BOLETO,
                value=11.42,
                dueDate=date(year=2024, month=7, day=20),
            ),
        )

        assert payment.value == 11.42


class TestAsaasAllPayment:
    def test_all_payment(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        all_payments = asaas_svc.payment.all()

        assert all_payments.data is not None
        assert isinstance(all_payments.data[0], PaymentViewSchema)

    def test_all_payment_filter_dto(self):
        filter_by = PaymentFilterBy(
            dateCreated_ge=date(2024, 7, 19), dueDate_le=date(2024, 8, 3)
        ).as_lean_dict()

        assert {
            "dateCreated[ge]": "2024-07-19",
            "dueDate[le]": "2024-08-03",
        } == filter_by

    def test_all_payment_with_filter(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        filtered_payments = asaas_svc.payment.all(status="RECEIVED")

        assert filtered_payments.totalCount == 2


class TestAsaasDeletePayment:
    def test_delete_payment(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        has_deleted = asaas_svc.payment.delete(payment_id="pay_vtkxai01k8o8jo55")

        assert has_deleted


class TestAsaasGetWrongPayment:
    def test_get_payment(self, asaas_svc):
        asaas_svc: AsaasService = asaas_svc

        with pytest.raises(AsaasClientError) as exc_info:
            asaas_svc.payment.get("pay_that_not_exists")

        assert exc_info.value.status_code == 404
        assert exc_info.value.message == ""
        assert exc_info.value.details is None
