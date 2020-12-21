from accounts.api.viewsets import ProductViewSet, OrderViewSet, CustomerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('customers', CustomerViewSet)
