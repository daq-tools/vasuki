import pytest
import vasuki.api


@pytest.fixture
def api():
    return vasuki.api.api
