from rest_framework import serializers

from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ListCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'price', 'is_active', 'rating', 'language')


class StudentsCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsCourses
        fields = '__all__'


class LIstModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'title', 'description')