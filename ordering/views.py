from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ordering.models import Collection, Product, Restaurant
from ordering.serializers import CollectionSerializer, ProductSerializer, RestautantSerializer
from django.db.models.aggregates import Count
# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['restaurant_id', 'collection_id']
    search_fields = ['title']
    ordering_fields = ['collection_id']

    def get_serializer_context(self):
        return {'request': self.request}


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestautantSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_context(self):
        return {'request': self.request}
