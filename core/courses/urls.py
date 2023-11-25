from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:id>/', CourseAPIView.as_view(), name='course'),
    path('modules/', ModuleListAPIView.as_view(), name='get-modules'),
    path('modules/<int:id>/', ModuleAPIView.as_view(), name='module'),
    path('enroll/<int:id>/', EnrollCourseAPIView.as_view(), name='enroll'),
    path('unenroll/<int:enroll_id>/', EnrollCourseAPIView.as_view(), name='unenroll'),
    path('lessons/<int:lesson_id>/', LessonAPIView.as_view(), name='lesson'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('video-content/', VideoContentListAPIView.as_view(), ),
    path('video-content/<int:content_id>/', VideoContentAPIView.as_view(), ),
    path('lessons/<int:id>/image-content/', ImageContentListAPIView.as_view(), ),
    path('lessons/<int:id>/image-content/<int:content_id>/', ImageContentAPIView.as_view(), ),
    path('lessons/<int:id>/video-content/', TextContentListAPIView.as_view(), ),
    path('lessons/<int:id>/video-content/<int:content_id>/', TextContentAPIView.as_view(), ),
]