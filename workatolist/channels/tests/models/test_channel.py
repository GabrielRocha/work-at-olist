import pytest
from channels.models import Channel
from django.db import models


@pytest.fixture
def channel():
    return Channel(name="Walmart")


def test_field_name_is_charfield():
    assert isinstance(Channel._meta.get_field('name'), models.CharField)


def test_field_slug_is_slugfield():
    assert isinstance(Channel._meta.get_field('slug'), models.SlugField)


@pytest.mark.django_db
def test_create_channel(channel):
    channel.save()
    assert Channel.objects.filter(name='Walmart').count() == 1


@pytest.mark.django_db
def test_slug_channel(channel):
    channel.save()
    assert Channel.objects.get(name='Walmart').slug == "walmart"
