from django.core.urlresolvers import reverse
import pytest


@pytest.mark.django_db
@pytest.mark.usefixtures('channel')
@pytest.mark.parametrize('url', ["/v1/channels/", reverse("channels:channel-list")])
def test_list_channels(client, url):
    response = client.get(url)
    assert response.json() == [{'name': 'Walmart',
                                'url': 'http://testserver/v1/channels/walmart/'}]


@pytest.mark.django_db
@pytest.mark.usefixtures('channel')
@pytest.mark.parametrize('url', ["/v1/channels/walmart/",
                                 reverse("channels:channel-detail", args=['walmart'])])
def test_detail_channel_without_categories(client, url):
    response = client.get(url)
    assert response.json() == {'name': 'Walmart', 'categories': []}


@pytest.mark.django_db
@pytest.mark.usefixtures('channel', 'category')
def test_detail_channel_with_category(client):
    response = client.get("/v1/channels/walmart/")
    assert response.json() == {'name': 'Walmart',
                               'categories': ['http://testserver/v1/category/walmart-books/']}
