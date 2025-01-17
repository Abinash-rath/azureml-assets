# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# flake8: noqa: F401,F403

"""Global test level fixtures."""

import pytest
import requests

from src.batch_score.common.telemetry.logging_utils import setup_logger
from tests.fixtures.adjustment import *
from tests.fixtures.completion_header_handler import *
from tests.fixtures.conductor import *
from tests.fixtures.input_transformer import *
from tests.fixtures.logging_utils import *
from tests.fixtures.parallel_driver import *
from tests.fixtures.quota_client import *
from tests.fixtures.routing_client import *
from tests.fixtures.scoring_client import *
from tests.fixtures.scoring_result import *
from tests.fixtures.tally_failed_request_handler import *
from tests.fixtures.token_provider import *
from tests.fixtures.vesta_encoded_image_scrubber import *
from tests.fixtures.vesta_image_modifier import *
from tests.fixtures.worker import *


@pytest.fixture(autouse=True, params=[pytest.param(None, marks=pytest.mark.unit)])
def mark_as_unit_test():
    """Mark all tests in this directory as unit tests."""
    pass


@pytest.fixture(autouse=True, params=[pytest.param(None, marks=pytest.mark.unit)])
def setup_logger_fixture():
    """Set up the logger for all tests in this directory."""
    setup_logger('DEBUG')


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    """Disable network calls."""
    def stunted_network_request():
        raise RuntimeError("Network access not allowed during unit testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_network_request())
    monkeypatch.setattr(requests, "put", lambda *args, **kwargs: stunted_network_request())
    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: stunted_network_request())
    monkeypatch.setattr(requests, "patch", lambda *args, **kwargs: stunted_network_request())
    monkeypatch.setattr(requests, "delete", lambda *args, **kwargs: stunted_network_request())
