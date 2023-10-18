from django.urls import path, include

from .views import *

urlpatterns = [
    # path('catalog', name='catalog')
    path('course/<int:pk>', CourseAPIView.as_view(), name='course')
]