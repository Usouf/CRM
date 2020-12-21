from accounts.models import Order
from django_filters import rest_framework as filters

class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'status': ['exact']
        }
