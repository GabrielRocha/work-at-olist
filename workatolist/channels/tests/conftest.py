import pytest
from channels.models import Channel


@pytest.fixture
def channel():
    return Channel(name="Walmart")
