from dataclasses import field, fields
from email.policy import default
from rest_framework import serializers
from ordering.models import Collection, Product, Restaurant


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True, default=0)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price',
                  'image_url', 'collection', 'restaurant']

    collection = serializers.PrimaryKeyRelatedField(
        queryset=Collection.objects.all()
    )
    restaurant = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all()
    )


class RestautantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'address', 'image_url']
