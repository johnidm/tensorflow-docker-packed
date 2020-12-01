import pytest

from myapp.app import app


@pytest.fixture
def client():
    return app.test_client()
