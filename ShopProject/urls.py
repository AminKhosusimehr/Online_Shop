from django.contrib import admin
from django.urls import path
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/' , include('Accounts.urls', namespace='Accounts')),
    path('api/' , include('Products.urls' , namespace='Products')),
]
