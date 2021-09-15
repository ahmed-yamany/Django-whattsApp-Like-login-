from django.urls import path, include
from .views import (
    home,
    register_or_login,
    verify_code,
    log_out
)
urlpatterns = [
    path('api/', include('users.api.urls'), name='user_api'),
    path('home/', home, name='home'),
    path('register_or_login/', register_or_login, name='user_register'),
    path('verify/', verify_code, name='verify_code'),
    path('logout/', log_out, name='logout'),

]
