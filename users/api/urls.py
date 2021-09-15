from django.urls import path, include
from .views import (
    user_api_links,
    register_or_login,
    verify_code,
    )
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user-api-links', user_api_links, name='user_api_links'),
    path('register_or_login', register_or_login, name='user_api_register'),
    path('verify', verify_code, name='user_api_register'),

]
