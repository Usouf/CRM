from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class ProductLimitPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 5

class OrderLimitPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 10

class CustomerLimitPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 10
