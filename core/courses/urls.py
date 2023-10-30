from django.urls import path, include

from .views import *

urlpatterns = [
    path('course/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('course-delete/<int:pk>/', CourseAPIView.as_view(), name='course-delete'),
    path('course-update/<int:pk>/', CourseAPIView.as_view(), name='course-update'),
    #path('course/modules/<int:pk>/', CourseModuleCRUD.as_view(), name='get-module'),#TODO Сделать метод get
    path('course/modules/<int:pk>/', CourseModuleCRUD.as_view(), name='get-module'),#TODO Сделать метод get
    path('course/modules/update/<int:pk>/', CourseModuleCRUD.as_view(), name='get-module'),#TODO сделать метод put
    path('course/modules/delete/<int:pk>/', CourseModuleCRUD.as_view(), name='get-module'),#TODO Сделать метод delete
    path('catalog/', CourseListAPIView.as_view(), name='catalog'),
    path('enroll/<int:id>/', EnrollCourseAPIView.as_view(), name='enroll'),
    path('unenroll/<int:id>/', EnrollCourseAPIView.as_view(), name='unenroll'),
]