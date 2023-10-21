from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('rest_framework_social_oauth2.urls')),
]
