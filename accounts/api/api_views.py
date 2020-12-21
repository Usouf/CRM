from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.api.serializers import ProductSerializer
from accounts.models import Product

from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def apiProductsView(request, format = None):
    items = Product.objects.all()
    productsCount = items.count()
    products = ProductSerializer(items, many = True)
    content = {
        'count': productsCount,
        'data': products.data,
    }

    return Response(content)
