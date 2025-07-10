from .views import RegisterView
from django.urls import path

app_name = 'Accounts'

urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),

]