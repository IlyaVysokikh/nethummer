from django.shortcuts import render
from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class CourseAPIView(APIView):
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs['pk'])
        serializer = CourseSerializer(course)
        return Response(serializer.data)
