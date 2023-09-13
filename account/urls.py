from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('emai_verify/',VerifyEmail.as_view(),name="email-verify"),
    ]