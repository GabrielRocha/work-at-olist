import pytest
from channels.models import Category


@pytest.mark.django_db
def test_create_first_level_category_slug(category):
    assert category.slug == "walmart-books"


@pytest.mark.django_db
def test_create_first_level_category_channel(category, channel):
    assert category.channel == channel


@pytest.mark.django_db
def test_create_second_level_category_foreign_key(category, channel):
    second_level_category = Category.objects.create(channel=channel, name="Comedy", parent=category)
    assert second_level_category.channel == channel
    assert second_level_category.parent.name == "Books"


@pytest.mark.django_db
def test_create_second_level_category_slug(category, channel):
    second_level_category = Category.objects.create(channel=channel, name="Comedy", parent=category)
    assert second_level_category.slug == 'walmart-books-comedy'
