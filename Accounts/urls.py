from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterView , TokenObtainPairView
from django.urls import path

app_name = 'Accounts'

urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]