import pytest
from channels.models import Channel, Category
from django.db import models


def test_field_name_is_charfield():
    assert isinstance(Channel._meta.get_field('name'), models.CharField)


def test_field_slug_is_slugfield():
    assert isinstance(Channel._meta.get_field('slug'), models.SlugField)


@pytest.mark.django_db
@pytest.mark.usefixtures('channel')
def test_create_channel():
    assert Channel.objects.filter(name='Walmart').count() == 1


@pytest.mark.django_db
def test_slug_channel(channel):
    assert channel.slug == "walmart"


@pytest.mark.django_db
def test_channels_categories(channel, category):
    assert channel.categories.count() == 1
    assert category in channel.categories.iterator()


@pytest.mark.django_db
def test_channels_two_levels_categories(channel, category):
    second_level_category = Category.objects.create(channel=channel,
                                                    name="Comedy", parent=category)
    assert second_level_category in channel.categories.first().get_descendants()


@pytest.mark.django_db
def test_channels_three_levels_categories(channel, category):
    second_level_category = Category.objects.create(channel=channel,
                                                    name="Comedy", parent=category)
    third_level_category = Category.objects.create(channel=channel,
                                                    name="Studio", parent=second_level_category)
    assert third_level_category in channel.categories.first().get_descendants()


@pytest.mark.django_db
def test_str_channel(channel):
    assert str(channel) == 'walmart'
