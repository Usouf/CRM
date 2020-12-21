from accounts.models import Product, Order, Customer
from .serializers import ProductSerializer, OrderSerializer, CustomerSerializer
from rest_framework import viewsets
from .pagination import ProductLimitPagination, OrderLimitPagination, CustomerLimitPagination
from .viewsetfilters import OrderFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductLimitPagination

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderLimitPagination
    filterset_class = OrderFilter


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomerLimitPagination
