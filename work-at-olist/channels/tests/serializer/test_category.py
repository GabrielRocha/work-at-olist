from django.core.urlresolvers import reverse
import pytest

from channels.models import Category


@pytest.mark.django_db
@pytest.mark.usefixtures('channel', 'category')
@pytest.mark.parametrize('url', ["/v1/category/walmart-books/",
                                 reverse("channels:category-detail",
                                         args=['walmart-books'])])
def test_detail_category(client, url):
    response = client.get(url)
    expected = {'parent': None,
                'name': 'Books', 'subcategories': []}
    assert response.json() == expected


@pytest.mark.django_db
def test_detail_category_with_subcategories(client, category, channel):
    Category.objects.create(name="Comedy", channel=channel, parent=category)
    subcategories = {'parent': 'http://testserver/v1/category/walmart-books/',
                     'name': 'Comedy', 'subcategories': []}
    expected = {'parent': None,
                'name': 'Books', 'subcategories': [subcategories]}
    response = client.get("/v1/category/walmart-books/")
    assert response.json() == expected
