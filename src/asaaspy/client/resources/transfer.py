from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.transfer import (
    TransferFilterBy,
    TransferItemViewSchema,
    TransferSchema,
)


class TransferResource(AsaasResource):
    def get_transfers(self, **transfer_filter_by):
        transfer_filter_by = TransferFilterBy(**transfer_filter_by)

        response = self.get_list_response(
            self.call(
                "GET",
                "v3/transfers",
                params=transfer_filter_by.as_lean_dict()
                if transfer_filter_by
                else None,
            ),
            data_response_class=TransferItemViewSchema,
        )
        return response

    def get_by_id(self, transfer_id) -> TransferItemViewSchema:
        response = self.call("GET", f"v3/transfers/{transfer_id}")
        return TransferItemViewSchema(**response)

    def create(self, transfer: TransferSchema) -> TransferItemViewSchema:
        response = self.call("POST", "v3/transfers", json=transfer.as_lean_dict())
        return TransferItemViewSchema(**response)

    def delete(self, id: str) -> TransferItemViewSchema:
        response = self.call("DELETE", f"v3/transfers/{id}/cancel")
        return TransferItemViewSchema(**response)
