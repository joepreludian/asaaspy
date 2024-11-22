from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.subaccount import (
    SubAccountViewSchema,
    SubAccountSchema,
    SubAccountFilterBySchema,
)


class SubAccountsResource(AsaasResource):
    def create(self, sub_account_schema: SubAccountSchema) -> SubAccountViewSchema:
        response = self.call(
            "POST", "v3/accounts", json=sub_account_schema.as_lean_dict()
        )
        return SubAccountViewSchema(**response)

    def get_by_id(self, id):
        response = self.call("GET", f"v3/accounts/{id}")
        return SubAccountViewSchema(**response)

    def list(self, **filters):
        filters = SubAccountFilterBySchema(**filters)
        return self.get_list_response(
            self.call("GET", "v3/accounts", params=filters.as_lean_dict()),
            SubAccountViewSchema,
        )
