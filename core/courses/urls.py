from django.urls import path, include

from .views import *

urlpatterns = [
    # path('catalog', name='catalog')
    path('course/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('catalog/', CourseListAPIView.as_view(), name='catalog'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll'),
    path('unenroll/<int:id>/', unenroll_course, name='unenroll')
]