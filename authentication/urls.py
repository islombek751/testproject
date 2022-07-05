from django.urls import path, include
from .views import *

register_logout_url = [
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('validate_activation_code/', CheckActivationCodeView.as_view()),
]

urlpatterns = [
    path('', include(register_logout_url)),
]