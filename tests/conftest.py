import logging
import os

import pytest
import vcr

from asaaspy.service import AsaasService


@pytest.fixture
def asaas_svc(caplog, mock_http_client):
    caplog.set_level(logging.INFO)

    return AsaasService(
        api_key=os.environ.get("ASAAS_SANDBOX_TOKEN"),
        sandbox=True,
    )


@pytest.fixture
def mock_http_client():
    with vcr.use_cassette(
        "./tests/asaas_sandbox_vcr.yml",
        serializer="json",
        record_mode="new_episodes",
        filter_headers=["access_token"],
    ):
        yield
