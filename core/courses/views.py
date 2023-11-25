from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .permissions import *
from .base_classes.views import *


class CourseAPIView(BaseAPIView):
    model = Course
    serializer_class = CourseSerializer
    permission_classes = [IsOwnerOrAdmin]


class ModuleAPIView(BaseAPIView):
    model = Module
    permission_classes = [IsOwnerOrAdmin]
    serializer_class = ModuleSerializer


class LessonAPIView(BaseAPIView):
    model = Lesson
    permission_classes = [IsOwnerOrAdmin]
    serializer_class = LessonSerializer


class TextContentAPIView(BaseAPIView):
    model = TextContent
    serializer_class = TextContentSerializer
    permission_classes = (IsOwnerOrAdmin)


class ImageContentAPIView(BaseAPIView):
    model = ImageContent
    serializer_class = ImageContentSerializer
    permission_classes = (IsOwnerOrAdmin)


class VideoContentAPIView(BaseAPIView):
    model = VideoContent
    serializer_class = VideoContent
    permission_classes = (IsOwnerOrAdmin)


class EnrollCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentsCoursesSerializer

    def post(self, request, id):
        course = get_object_or_404(Course, id=id)
        enrollment, created = StudentsCourses.objects.get_or_create(student=request.user, course=course)
        serializer = self.serializer_class(enrollment)
        return Response({
            'enrollment_created': created,
            'data': serializer.data
              })

    def delete(self, request, id):
        enrollment = get_object_or_404(StudentsCourses, id=id)
        enrollment.delete()
        return Response({
            'unenrolled': True
            }, status=status.HTTP_204_NO_CONTENT)


class StudentsCoursesListAPIView(ListAPIView):
    serializer_class = StudentsCoursesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = StudentsCourses.objects.filter(student=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CourseListAPIView(BaseListAPIView):
    model = Course
    serializer_class = CourseSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        queryset = Course.objects.filter(is_active=True)

        if category:
            queryset = queryset.filter(category=category)

        return queryset


class ModuleListAPIView(BaseListAPIView):
    model = Module
    serializer_class = ModuleSerializer


class LessonListAPIView(BaseListAPIView):
    model = Lesson
    serializer_class = LessonSerializer


class VideoContentListAPIView(BaseListAPIView):
    model = VideoContent
    serializer_class = VideoContentSerializer


class ImageContentListAPIView(ListAPIView):
    model = ImageContent
    serializer_class = ImageContentSerializer


class TextContentListAPIView(ListAPIView):
    model = TextContent
    serializer_class = TextContentSerializer
