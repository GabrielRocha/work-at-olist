from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^v1/', include('channels.urls', namespace="channels")),
    url(r'^v1/docs/', include_docs_urls(title='Olist API')),
]
