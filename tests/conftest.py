import logging
import os

import pytest
import vcr

from asaaspy.service import AsaasService


@pytest.fixture
def mock_http_client(request):
    root_path = request.config.rootdir
    with vcr.use_cassette(
        f"{root_path}/tests/asaas_sandbox_vcr.json",
        serializer="json",
        record_mode="new_episodes",
        filter_headers=["access_token"],
        match_on=["method", "scheme", "host", "port", "path", "query", "body"],
    ):
        yield


@pytest.fixture
def asaas_svc(caplog, mock_http_client):
    caplog.set_level(logging.INFO)

    return AsaasService(
        api_key=os.environ.get("ASAAS_SANDBOX_TOKEN"),
        sandbox=True,
    )


@pytest.fixture
def asaas_svc_subaccount(caplog, mock_http_client):
    caplog.set_level(logging.INFO)

    return AsaasService(
        api_key=os.environ.get("ASAAS_SANDBOX_TOKEN_SUBACCOUNT_1"),
        sandbox=True,
    )


@pytest.fixture
def document_test_as_file_handler(request):
    root_path = request.config.rootdir
    with open(f"{root_path}/tests/_assets/document_test.svg", "rb") as file_handler:
        yield file_handler
