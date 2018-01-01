import pytest
from channels.models import Channel, Category


@pytest.fixture
@pytest.mark.django_db
def channel():
    return Channel.objects.create(name="Walmart")


@pytest.fixture
@pytest.mark.django_db
def category(channel):
    return Category.objects.create(channel=channel, name="Books")
