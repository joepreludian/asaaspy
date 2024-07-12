import vcr
import pytest
from asaaspy.service import AsaasService
import logging


@pytest.fixture
def asaas_svc(caplog):
    caplog.set_level(logging.INFO)

    return AsaasService(
        APIKey="***REMOVED***",
        sandbox=True,
    )


@pytest.fixture
def mock_http_client():
    with vcr.use_cassette(
        "./tests/asaas_sandbox_vcr.yml", serializer="json", record_mode="new_episodes"
    ):
        yield
