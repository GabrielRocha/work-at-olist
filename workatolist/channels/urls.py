from django.conf.urls import url, include
from rest_framework import routers
from channels.views import ChannelView

router = routers.DefaultRouter()
router.register(r'channels', ChannelView, 'channel')

urlpatterns = [url(r'^', include(router.urls)),]
