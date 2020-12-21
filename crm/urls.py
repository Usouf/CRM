from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings
from accounts.api import api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api/', include(router.urls)),
    # path('api/', api_views.apiProductsView),
    path('api-token-auth/', views.obtain_auth_token, name = 'api-token-auth'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
