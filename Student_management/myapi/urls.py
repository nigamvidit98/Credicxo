from django.urls import re_path, path
from myapi.views import UserRegistrationView
from . import views

urlpatterns = [
    re_path(r'^signup', UserRegistrationView.as_view()),
    path('hello/', views.HelloView.as_view(), name ='hello'),
    ]