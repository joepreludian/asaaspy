from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.my_account import MyAccountDocumentsViewSchema


class MyAccountResource(AsaasResource):
    def get_pending_documents(self) -> MyAccountDocumentsViewSchema:
        response = self.call("GET", "v3/myAccount/documents")
        return MyAccountDocumentsViewSchema(**response)
