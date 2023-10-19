from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import *
from .serializers import *


class CourseAPIView(APIView):
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class CourseListAPIView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        queryset = Course.objects.filter(is_active=True)

        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)


def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enroll = StudentsCourses.objects.get_or_create(student=request.user, course=course)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unenroll_course(request, id):
    enroll = StudentsCourses.objects.get(id=id)
    enroll.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))