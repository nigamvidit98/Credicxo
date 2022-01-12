from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    path('', include('myapi.urls')),
    path('admin/', admin.site.urls)
]