from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from api.auth.views import *
from api.clothes.views import *
from api.order.views import *


urlpatterns = [
    ### clothes List
    path("clothing-items/", ClothingItemsView.as_view(), name="clothing-items"),
    path("clothing-item/<int:pk>/", ClothingItemDetail.as_view(), name="clothing-item"),
    
    ### EndPoints for Orders
    path("order-list/", OrderListView.as_view(), name="order-list"),
    path("order-item/<int:pk>/", OrderItemView.as_view(), name="order-item"),
    path("create-order/", CreateOrderView.as_view(), name="create-order"),
    
    ### endpoinst for register and login
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    
    ### EndPoint for User Profile
    path("profile/", ProfileView.as_view(), name="profile"),
]
