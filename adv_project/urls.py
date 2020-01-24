from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    re_path(r'^api-token-auth/', views.obtain_auth_token)
]
