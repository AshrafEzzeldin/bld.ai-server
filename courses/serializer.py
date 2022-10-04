from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
