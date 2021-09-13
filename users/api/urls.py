from django.urls import path, include
from .views import (
    user_api_links, register
    )

urlpatterns = [
    path('user-api-links', user_api_links, name='user_api_links'),
    path('register', register, name='user_api_register')
]
