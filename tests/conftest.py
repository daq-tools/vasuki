import pytest


@pytest.fixture
def api():
    import vasuki.api

    return vasuki.api.api
