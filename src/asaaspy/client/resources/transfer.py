from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.transfer import TransferFilterBy, TransferItemViewSchema


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

    def get_by_id(self, transfer_id):
        response = self.call("GET", f"v3/transfers/{transfer_id}")
        return TransferItemViewSchema(**response)