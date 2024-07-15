import httpx

from asaaspy.constants import APIBaseURL
from asaaspy.log import log
from asaaspy.schemas.base import PaginatedOutputPayload


class AsaasClient:
    def __init__(self, api_key, sandbox=False) -> None:
        self._client_params = {
            "headers": {
                "Content-Type": "application/json",
                "User-Agent": "AsaasPy",
                "access_token": api_key,
            },
            "base_url": (
                APIBaseURL.SANDBOX if sandbox else APIBaseURL.PRODUCTION
            ).value,
        }

        log.info(
            f"Initialized AsaasClient in {'sandbox' if sandbox else 'production'} mode"
        )

    def _get_http_client(self):
        log.info("Client instantiated")
        return httpx.Client(**self._client_params)


class AsaasResource:
    def __init__(self, asaas_client_instance):
        self._client = asaas_client_instance

    def get_client(self):
        return self._client._get_http_client()

    def get_list_response(
        self, response, data_response_class=dict
    ) -> PaginatedOutputPayload:
        # TODO: Work on a better way to handle HTTP RESPONSES
        response = PaginatedOutputPayload(**response.json())
        response.data = [data_response_class(**item) for item in response.data]

        return response
