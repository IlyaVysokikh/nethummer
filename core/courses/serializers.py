from rest_framework import serializers

from .models import *


class StudentsCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsCourses
        fields = '__all__'
        

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class TextContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextContent
        fields = '__all__'


class VideoContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoContent
        fields = '__all__'


class ImageContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageContent
        fields = '__all__'