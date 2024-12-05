from asaaspy.client.base import AsaasResource
from asaaspy.schemas.v3.my_account import (
    MyAccountDocumentsViewSchema,
    MyAccountStatusViewSchema,
)
from asaaspy.schemas.v3.my_account import MyAccountSendDocumentViewSchema


class MyAccountResource(AsaasResource):
    def get_pending_documents(self) -> MyAccountDocumentsViewSchema:
        response = self.call("GET", "v3/myAccount/documents")
        return MyAccountDocumentsViewSchema(**response)

    def send_document(
        self, document_id, type, file_handler
    ) -> MyAccountSendDocumentViewSchema:
        response = self.call(
            "POST",
            f"v3/myAccount/documents/{document_id}",
            files={"documentFile": (file_handler.name.split["/"][-1], file_handler)},
            json={"type": type},
        )
        return MyAccountSendDocumentViewSchema(**response)

    def get_status(self):
        response = self.call("GET", "v3/myAccount/status")
        return MyAccountStatusViewSchema(**response)
