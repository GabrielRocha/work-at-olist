from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from channels.models import Channel, Category
from channels.serializer import ChannelListSerializer, ChannelDetailSerializer, CategorySerializer


class ChannelView(viewsets.ViewSet):
    """ List all channels """
    lookup_field = 'slug'

    def list(self, request, *args):
        channels = Channel.objects.all()
        serializer = ChannelListSerializer(channels, many=True,
                                           context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        channels = get_object_or_404(Channel, slug=slug)
        serializer = ChannelDetailSerializer(channels, context={'request': request})
        return Response(serializer.data)


class CategoryView(viewsets.ViewSet):
    """ Detail category """

    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        category = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)
