from rest_framework.routers import DefaultRouter
from django.urls import path, include

from Products import views


app_name = 'Products'

router = DefaultRouter()

router.register(r'', views.ProductViewSet)

urlpatterns = [
    path('' , include(router.urls)),
]