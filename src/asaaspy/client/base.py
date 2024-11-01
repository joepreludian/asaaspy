from json.decoder import JSONDecodeError

import httpx

from asaaspy.constants import APIBaseURL
from asaaspy.exceptions import AsaasClientError
from asaaspy.log import log
from asaaspy.schemas.base import PaginatedViewSchema


class AsaasHTTPClient:
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

    def get_http_client(self):
        log.info("Client instantiated")
        return httpx.Client(**self._client_params, timeout=30)


class AsaasResource:
    def __init__(self, asaas_client_instance):
        self._client = asaas_client_instance

    def get_client(self):
        return self._client.get_http_client()

    def call(self, *args, **kwargs):
        with self._client.get_http_client() as client:
            request = client.build_request(*args, **kwargs)
            response = client.send(request)

            if response.status_code not in [
                200,
                202,
                203,
                204,
                205,
                206,
                207,
                208,
            ]:  # TODO think in a better way
                try:
                    error_data = response.json()
                except JSONDecodeError:
                    error_data = None

                response_text = (
                    error_data["errors"][0]["description"]
                    if error_data
                    else response.text
                )
                raise AsaasClientError(
                    message=response_text,
                    status_code=response.status_code,
                    details=error_data,
                )

            return response.json()

    def get_list_response(
        self, response, data_response_class=dict
    ) -> PaginatedViewSchema:
        # TODO: Work on a better way to handle HTTP RESPONSES
        response = PaginatedViewSchema(**response)
        response.data = [data_response_class(**item) for item in response.data]

        return response
