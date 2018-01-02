from rest_framework import serializers
from channels.models import Channel


class ChannelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'url')
        extra_kwargs = {
            'url': {'lookup_field': 'slug', 'view_name': 'channels:channel-detail'}
        }


class ChannelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'categories')
