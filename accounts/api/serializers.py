from rest_framework import serializers
from accounts.models import Product, Order, Customer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'description')

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='getProductName')
    date_time_created = serializers.CharField(source='getDateTime')
    class Meta:
        model = Order
        fields = ('id', 'product', 'product_name', 'date_time_created', 'status')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'phone', 'email')
