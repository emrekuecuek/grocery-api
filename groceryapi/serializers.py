from rest_framework import serializers
from .models import User, TransactionStory, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'street_address', 'zip_code', 'phone', 'customer_id']

class TransactionStorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionStory
        fields = ['customer_id', 'basket', 'purchase_count']

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'product_type']
