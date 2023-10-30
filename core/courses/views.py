from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .permissions import *


class CourseAPIView(APIView):
    serializer_class = CourseSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_course(self, pk):
        try:
            return Course.objects.get(id=pk)
        except:
            return None

    def get(self, request, *args, **kwargs):
        course = self.get_course(pk=kwargs['pk'])

        if not course:
            return Response({
                'status': 'fail',
                'message': f'Курс с id = {kwargs["pk"]} не найден'
            },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(course)

        return Response({
            'status': 'success',
            'course': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        course = self.get_course(pk)

        if not course:
            return Response({
                'status': 'fail',
                'message': f'Курс с id = {pk} не найден'
            },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'course': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': 'fail',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_course(pk)

        if not course:
            return Response({
                'status': 'fail',
                'message': f'Курс с id = {pk} не найден'
            },
                status=status.HTTP_404_NOT_FOUND
            )

        course.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class CourseListAPIView(ListAPIView):
    serializer_class = ListCourseSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        queryset = Course.objects.filter(is_active=True)

        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class EnrollCourseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentsCoursesSerializer

    def post(self, request, id):
        course = get_object_or_404(Course, id=id)
        enrollment, created = StudentsCourses.objects.get_or_create(student=request.user, course=course)
        serializer = self.serializer_class(enrollment)
        return Response({'enrollment_created': created, 'data': serializer.data})

    def delete(self, request, id):
        enrollment = get_object_or_404(StudentsCourses, id=id)
        enrollment.delete()
        return Response({'unenrolled': True}, status=status.HTTP_204_NO_CONTENT)


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
