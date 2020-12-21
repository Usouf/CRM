from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

    path('', views.home, name = "home"),
    path('user/', views.userPage, name = "user_page"),
    path('account/', views.accountSettings, name = "account"),
    path('products/', views.products, name = "products"),
    path('customer/<int:pk>', views.customer, name = "customer"),

    path('create_product/', views.createProducts, name = "create_product"),
    path('create_order/<int:pk>', views.createOrder, name = "create_order"),
    path('update_order/<int:pk>', views.updateOrder, name = "update_order"),
    path('delete_order/<int:pk>', views.deleteOrder, name = "delete_order"),

    path('upload_pdf', views.uploadPdf, name="upload"),
]
