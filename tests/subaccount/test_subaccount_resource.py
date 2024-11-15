from asaaspy.schemas.v3.subaccount import SubAccountSchema
from schemas.v3.subaccount import SubAccountViewSchema


class TestSubAccountResource:
    def test_create_minimal_subaccount_physical_person(self, asaas_svc):
        request_subaccount = SubAccountSchema(
            name="Porco Rosso",
            email="porco.rosso@asaaspy.com.br",
            cpfCnpj="751.493.120-10",
            mobilePhone="41991524243",
            incomeValue=10000,
            address="Avenida Pres. Epitácio Pessoa",
            addressNumber="2690",
            province="Tambauzinho",
            postalCode="58042006",
            birthDate="1988-12-13",
        )

        account_result = asaas_svc.sub_accounts.create(request_subaccount)

        assert isinstance(account_result, SubAccountViewSchema)
        assert account_result.name == "Porco Rosso"
        assert isinstance(account_result.walletId, str)
        assert isinstance(account_result.apiKey, str)
        assert account_result.apiKey.startswith("$aact_YT")
