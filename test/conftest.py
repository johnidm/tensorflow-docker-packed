import pytest

from app.app import app


@pytest.fixture
def client():
    return app.test_client()
