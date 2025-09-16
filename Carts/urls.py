from django.urls import include , path
from rest_framework.routers import DefaultRouter

from Carts import views

app_name = 'carts'

router = DefaultRouter()

router.register(r'carts', views.CartItemViewSet, basename='carts')

urlpatterns = [
    path('', include(router.urls)),
]