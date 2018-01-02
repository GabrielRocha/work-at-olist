from django.conf.urls import url, include
from rest_framework import routers
from channels.views import ChannelView, CategoryView

router = routers.DefaultRouter()
router.register(r'channels', ChannelView, 'channel')
router.register(r'category', CategoryView, 'category')

urlpatterns = [url(r'^', include(router.urls))]
