from rest_framework import serializers
from channels.models import Channel, Category
from rest_framework_recursive.fields import RecursiveField


class ChannelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('name', 'url')
        extra_kwargs = {
            'url': {'lookup_field': 'slug', 'view_name': 'channels:channel-detail'}
        }


class ChannelDetailSerializer(serializers.ModelSerializer):
    categories = serializers.HyperlinkedRelatedField(many=True, lookup_field='slug', read_only=True,
                                                     view_name='channels:category-detail')

    class Meta:
        model = Channel
        fields = ('name', 'categories')


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.ListSerializer(child=RecursiveField())
    parent = serializers.HyperlinkedRelatedField(lookup_field='slug', read_only=True,
                                                 view_name='channels:category-detail')

    class Meta:
        model = Category
        lookup_field = 'slug'
        fields = ("parent", "name", "subcategories")
